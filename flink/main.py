from db_utils import CassandraDb
from json_utils import load_json_data
import os

if __name__ == '__main__':

    file_path = os.path.join('..' ,'dataset', 'non-vpn2016', '2_training_set', '2_training_set.json')

    db = CassandraDb('127.0.0.1', 0, 'ost_sm_2020')

    # data = load_json_data(file_path)
    # db.insert_batch_data( data, table='non_vpn' )
