from typing import Dict, List

from pymongo import MongoClient
from services.mongodb.configurations import DB_NAME, DB_URI, LOGGER

from werkzeug.local import LocalProxy


class MongoFactory:
    @staticmethod
    def get_db():
        """
        Configuration method to return db instance
        """
        client = MongoClient(DB_URI)
        db = client[DB_NAME]

        if db is None:
            db = MongoClient(DB_URI,
                             maxPoolSize=50,
                             serverSelectionTimeoutMS=2500
                             )[DB_NAME]
        return db

    def server_status(self):
        return self.get_db().command('serverStatus')

    def get_configuration(self):
        """
        Returns the following information configured for this client:
        - max connection pool size
        - write concern
        - database user role
        """

        try:
            db = self.get_db()
            role_info = db.command({'connectionStatus': 1}).get('authInfo').get('authenticatedUserRoles')[0]
            print(db.client.max_pool_size, db.client.write_concern, role_info)
            return db.client.max_pool_size, db.client.write_concern, role_info
        except IndexError:
            return self.db.client.max_pool_size, self.db.client.write_concern, {}

    def insert_sample_collection(self):
        db = self.get_db()
        collection = db.sample_collection

        sample_row = {
            "_id": 4,
            "name": "sample_row"
        }
        collection.insert(sample_row)
        LOGGER.info(collection.find_one())

    def insert_row(self, _id, row, type:str, collection_name: str, verbose=False):
        db = self.get_db()

        if not type:
            LOGGER.warning("Dataset type should be denoted")
            raise

        collection_name = f'{collection_name}_{type}'
        collection = db[collection_name]

        collection.insert({"_id": _id,
                           "features": row
                           })
        if verbose:
            LOGGER.info(collection.find_one())