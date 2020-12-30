from db_utils import CassandraDb
from json_utils import load_json_data
import os
from config import config

if __name__ == '__main__':

    base_path = os.path.join( '..' , 'dataset',
        'non-vpn2016', '2_training_set')

    file_path = os.path.join( base_path, '2_training_set_m.json.gz' )

    labels_path = os.path.join( base_path, '2_training_anno_top.json.gz' )

    db = CassandraDb(config["ip_addr"], config["port"])

    db.export_table_to_csv(config['keyspace'], 'bytes_in_avg_sink', ['id', 'dst_port', 'bytes_in_avg'])
