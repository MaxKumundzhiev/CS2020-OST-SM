from db_utils import CassandraDb
from json_utils import load_json_data
import os

if __name__ == '__main__':

    base_path = os.path.join( '..' , 'dataset',
        'non-vpn2016', '2_training_set')

    file_path = os.path.join( base_path, '2_training_set_m.json.gz' )

    labels_path = os.path.join( base_path, '2_training_anno_top.json.gz' )

    keyspace = 'ost_sm_2020'
    table_name = 'non_vpn'

    ip_addr = ['127.0.0.1']

    db = CassandraDb(ip_addr, 9042)

    # db.create_keyspace(keyspace)

    fields = [
        'pr int',
    	'rev_intervals_ccnt list<int>',
    	'rev_pld_max int',
    	'dst_port int',
    	'num_pkts_in int',
    	'pld_ccnt list<int>',
    	'rev_hdr_ccnt list<int>',
    	'rev_hdr_bin_40 int',
    	'bytes_in int',
    	'rev_ack_psh_rst_syn_fin_cnt list<int>',
    	'time_length double',
    	'da text',
    	'rev_pld_var double',
    	'pld_mean double',
    	'rev_pld_mean double',
    	'pld_median int',
    	'src_port int',
    	'rev_pld_bin_128 int',
    	'sa text',
    	'hdr_distinct int',
    	'rev_pld_distinct int',
    	'ack_psh_rst_syn_fin_cnt list<int>',
    	'pld_distinct int',
    	'tls_svr_key_exchange_len int',
    	'hdr_bin_40 int',
    	'rev_pld_ccnt list<int>',
    	'tls_svr_cs_cnt int',
    	'tls_key_exchange_len int',
    	'tls_svr_ext_cnt int',
    	'tls_svr_ext_types list<text>',
    	'tls_ext_cnt int',
    	'tls_svr_cs list<text>',
    	'intervals_ccnt list<int>',
    	'hdr_ccnt list<int>',
    	'pld_bin_inf int',
    	'tls_ext_types list<text>',
    	'hdr_mean double',
    	'tls_len list<int>',
    	'tls_svr_len list<int>',
    	'num_pkts_out int',
    	'tls_svr_cnt int',
    	'tls_cs_cnt int',
    	'tls_cs list<text>',
    	'rev_hdr_distinct int',
    	'pld_max int',
    	'id bigint',
    	'tls_cnt int',
    	'bytes_out int',
    	'dns_answer_ip list<text>',
    	'http_uri text',
    	'dns_answer_cnt int',
    	'dns_query_name list<text>',
    	'dns_query_name_len list<int>',
    	'http_code int',
    	'dns_query_type list<int>',
    	'http_host text',
    	'dns_query_cnt int',
    	'dns_query_class list<int>',
    	'http_content_type text',
    	'http_content_len int',
    	'dns_answer_ttl list<int>',
    	'http_method int',
    	'PRIMARY KEY (id)'
    ]

    # db.alter_table(keyspace, table_name, 'label', 'text')
    # db.create_table( keyspace, table_name, fields)
    # data = load_json_data(file_path)

    labels = load_json_data( labels_path )

    ids, new_vals = [ int(id) for id in labels.keys() ], labels.values()

    db.update_records( keyspace, table_name, ids, 'label', new_vals )
    # db.insert_batch_data( data, table='non_vpn' )
