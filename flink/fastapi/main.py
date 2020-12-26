from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import sys
import json

sys.path.insert(0, '..')

from db_utils import CassandraDb

app = FastAPI()

db = CassandraDb( ['127.0.0.1'], 9042)

data = list()

def load_from_db(tablename):

    return db.read_table('ost_sm_2020', tablename)

def data_generator(tablename):
    global data
    # load data into memory
    if len( data ) == 0:
        data = load_from_db(tablename)

    for row in data:
        yield json.dumps( row ) + "\r\n"

@app.get("/{tablename}")
def read_all_data(tablename: str):
    return StreamingResponse(data_generator(tablename))
