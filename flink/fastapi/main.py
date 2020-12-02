from fastapi import FastAPI
import sys

sys.path.insert(0, '..')

from db_utils import CassandraDb

app = FastAPI()

db = CassandraDb( '127.0.0.1', 0, 'ost_sm_2020' )

@app.get("/{tablename}")
def read_all_data(tablename: str):
    return db.read_table(tablename)[0]
