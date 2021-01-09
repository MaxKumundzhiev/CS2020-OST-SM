from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import sys
import json
import threading

sys.path.insert(0, '..\\..\\..\\cassandradb')

from db_utils import CassandraDb

app = FastAPI()

db = CassandraDb( ['127.0.0.1'], 9042)

def load_from_db(tablename):

    return db.read_table('ost_sm_2020', tablename)

def data_generator(data):

    limit = len(data) - 1
    for i, row in enumerate( data ):
        if i < limit:
            yield json.dumps( row ) + "\r\n"
        else:
            yield "EOF" + "\r\n"

# load data into memory
non_vpn = load_from_db('non_vpn')

# non_vpn_test_std = load_from_db('non_vpn_test_std_preprocessed')
non_vpn_test_challenge = load_from_db('non_vpn_test_challenge')

print('booting up is completed...')

@app.get("/non_vpn")
def read_all_data():

    return StreamingResponse(data_generator(non_vpn))

@app.get("/non_vpn/test/{type}")
def read_all_data(type: str):
    if type == 'std':
        return StreamingResponse(data_generator(non_vpn_test_std))
    else:
        return StreamingResponse(data_generator(non_vpn_test_challenge))
