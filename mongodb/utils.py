from typing import Dict, List

from pymongo import MongoClient
from mongodb.config import DB_NAME, DB_URL, LOGGER


class Factory:
    def __init__(self):
        self.cursor = self._get_cursor()

    @staticmethod
    def _get_cursor():
        """Access database
        Note:
            if database does not exist it will be automatically created
        """

        try:
            client = MongoClient(DB_URL)
            db_cursor = client[DB_NAME]
            LOGGER.info(f'Accessed to {DB_NAME} database')
            return db_cursor
        except Exception as e:
            raise e

    def _get_collection(self, collection_name: str):
        """Access particular database collection
        Note:
            if collection does not exist it will be automatically created
        """

        try:
            db_collection = self.cursor[collection_name]
            LOGGER.info(f'Created to {collection_name} collection')
            return db_collection
        except Exception as e:
            raise e

    @staticmethod
    def _insert_row(collection, data: Dict):
        LOGGER.info(f'Inserted {len(data)} rows to {collection}')
        collection.insert_one(data)
        return True

    @staticmethod
    def _insert_rows(collection, data: List[Dict]):
        collection.insert_many(data)
        LOGGER.info(f'Inserted {len(data)} rows to {collection}')
        return True

    def run(self, data):
        collection = self._get_collection(collection_name=f'logs')  # collection name
        
        if len(data) != 1:
            self._insert_rows(collection, data=data)
        else:
            self._insert_row(collection, data=data)

        LOGGER.info(f'SUCCESS WRITE TO MG_DB')





