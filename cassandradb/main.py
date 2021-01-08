from db_utils import CassandraDb
from json_utils import load_json_data
import numpy as np
import pandas as pd
import os
import sys
import pickle
from config import config

def init_options():

    return [
        '--create-table', '--schema', '--insert-data', '--table-name', '--dataset'
    ]

def standardize_data(scaler, dataset):
    '''
        - remove mean and scale variance to unit vector for a dataset
        - parameters:
        -- scaler: the standard scaler object
        -- dataset: data set represented as a dataframe
    '''
    # save the id column, and then drop it
    id = dataset['id']
    dataset = dataset.drop(columns=['id'])

    X = dataset.to_numpy()
    # get all columns
    columns = dataset.columns

    # scale the test data set
    x_scaled = scaler.transform( X )

    dataset_scaled = pd.DataFrame(data=x_scaled, columns=columns)
    dataset_scaled['id'] = id

    return dataset_scaled.to_dict('records')


def create_insert_index_file():
    '''
        a backup utility for memorizing the index of the record inserted inside Cassandra
    '''
    with open('insert_index.txt', 'w') as f:
        f.write(str(0))

def reset_insert_index_file():
    '''
        Reseting the index of the last inserted row to 0 (first row)
    '''
    if not os.path.exists('insert_index.txt'):
        create_insert_index_file()
    else:
        with open('insert_index.txt', 'w') as f:
            f.write(str(0))

def load_start_index():

    with open('insert_index.txt', 'r') as file:
        return int( file.read() )

def load_standard_scaler(path):
    '''
        load a stored standard scaler from a file
    '''
    with open(path, 'rb') as s:
        scaler = pickle.load(s)
    return scaler

def create_table(db, args, config):

    '''
        create table command!
    '''

    table_name = str()
    schema = str()
    dataset = str()

    global data

    for i, arg in enumerate(args):
        if arg == '--create-table':
            table_name = args[i + 1]
        if arg == '--schema':
            schema = args[i + 1]
        if arg == '--dataset':
            dataset = args[i + 1]

    if schema not in config:
        print('WARNING: schema is not predefined in Config file. The schema will be inferred from data set!')

        training_file_path, _, _ = build_path(dataset)
        data = load_json_data(training_file_path, line_by_line=True)
        schema = db.build_schema(data)

        db.create_table(config['keyspace'], table_name, schema)
    else:
        db.create_table(config['keyspace'], table_name, config[schema])

def insert_data(db, args, config, reset_index=True):
    '''
        - insert data into some Cassandra partition
        - parameters:
        -- db: Database Instance
        -- args: arguments list
        -- config: configuration object
        -- reset_index = True, a simple fault-tolerance scenario in case the connection went down during data insertion. By default It is True, meaning we are starting a new insertion
    '''

    dataset = str()
    table_name = str()

    global data

    # reset insert batch data starting index
    if reset_index == True:
        reset_insert_index_file()

    for i, arg in enumerate(args):
        if arg == '--insert-data':
            dataset = args[i + 1]
        if arg == '--table-name':
            table_name = args[i + 1]
    training_file_path, labels_path, test_file_path = build_path(dataset)

    if len(data) == 0:
        data = load_json_data(training_file_path, line_by_line=True)

    labels = load_json_data(labels_path, line_by_line=False)

    # load starting index
    start_index = load_start_index()

    # call db.insert_batch_data(...)
    db.insert_batch_data(data, config['keyspace'], table_name, start_index)

    # attach labels to corresponding flows
    db.update_records(config['keyspace'], table_name, labels.keys(), 'label', labels.values())

def build_path(dataset):

    '''
        a utility function for building the path to a dataset
    '''

    # Path to Various Datasets files
    base_path = os.path.join( '..' , 'dataset', dataset)
    training_file_path = os.path.join( base_path,'2_training_set', '2_training_set.json.gz' )
    labels_path = os.path.join( base_path,'2_training_annotations', '2_training_anno_top.json.gz' )
    test_file_path = os.path.join( base_path, '0_test-challenge_set', '0_test-challenge_set.json.gz' )

    return training_file_path, labels_path, test_file_path

# entry point ---->
if __name__ == '__main__':

    # Check the correctness of options
    options = init_options()
    args = sys.argv[1:]

    data = list()

    for arg in args:
        if arg != '' and  arg not in options and '--' in arg:
            print('ERROR:{} Not Found!'.format(arg))
            sys.exit(1)

    # Initialize Database Instance
    db = CassandraDb(config["ip_addr"], config["port"])

    # process user request ---->
    if '--create-table' in args:
        create_table(db, args, config)

    elif '--insert-data' in args:
        insert_data(db, args, config)
