import json
import gzip

def load_json_data(file_path):

    if 'gz' in file_path:
        with gzip.open( file_path, 'rb' ) as f:
            return json.load( f )

    else:
        with open(file_path, 'r') as f:
            return json.load( f )
