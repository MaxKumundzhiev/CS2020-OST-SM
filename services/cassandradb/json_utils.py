import json
import gzip
import pandas as pd

features =  ['pr', 'id', 'rev_intervals_ccnt', 'rev_pld_max', 'dst_port', 'num_pkts_in', 'pld_ccnt', 'rev_hdr_ccnt', 'rev_hdr_bin_40', 'bytes_in',
        'rev_ack_psh_rst_syn_fin_cnt','time_length','rev_pld_var','pld_mean','rev_pld_mean', 'pld_median','src_port',
        'rev_pld_bin_128','hdr_distinct','rev_pld_distinct','ack_psh_rst_syn_fin_cnt','pld_distinct',
            'hdr_bin_40','rev_pld_ccnt','intervals_ccnt','hdr_ccnt',
            'pld_bin_inf','hdr_mean','num_pkts_out','rev_hdr_distinct',
            'pld_max','bytes_out']

def load_json_data(file_path, line_by_line=False, as_dataframe=False, preprocess=False):

    '''
        if as_dataframe is set to True, then preprocess must be set to true as well
        preprocess we drop all null attributes, and transform list-type attributes in a way
        where each element represents a dimension.
    '''
    if line_by_line:
        with gzip.open( file_path, 'rb' ) as f:
            return read_json(f, as_dataframe, preprocess)
    else:
        with gzip.open( file_path, 'rb' ) as f:
            return json.load( f )

def read_json(f, as_dataframe, preprocess):

    if as_dataframe:
        data_preprocessed_dict = dict()
    data_preprocessed_list = list()
    for row in f.readlines():

        row = json.loads(row)

        if preprocess:
            preprocessed_row = preprocess_row(row)
            data_preprocessed_list.append( preprocessed_row )
        else:
            data_preprocessed_list.append( row )
        if as_dataframe and preprocess:
            data_preprocessed_dict = add_to_dict(
                    preprocessed_row,
                    data_preprocessed_dict
            )
        elif as_dataframe and not preprocess:
            raise Exception('Error cannot Construct DataFrames from List type')
    if not as_dataframe:
        if len( data_preprocessed_list ) == 0:
            return data_preprocessed_list[0]
        return data_preprocessed_list
    else:
        return pd.DataFrame.from_dict( data_preprocessed_dict )

def preprocess_row(row):
    preprocessed_row = dict()
    for feature in features:
        if type( row[feature] ) is list:
            for i, e in enumerate(row[feature]):
                preprocessed_row[feature+'_'+str(i)] = row[feature][i]
        else:
            preprocessed_row[feature] = row[feature]
    return preprocessed_row

def add_to_dict(preprocessed_row, data_preprocessed):
    for k,v in preprocessed_row.items():
        if k not in data_preprocessed:
            values = list()
            values.append(v)
            data_preprocessed[k] = values
        else:
            values = data_preprocessed[k]
            values.append(v)
            data_preprocessed[k] = values
    return data_preprocessed
