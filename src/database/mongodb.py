import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        MONGO_DB_URL = "mongodb://localhost:27017/"
        #tlsCAFile=ca,
        self.client = pymongo.MongoClient(MONGO_DB_URL)
        self.db_name="ineuron"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
