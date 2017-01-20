__author__ = 'lin'
from connector.datasource import DataConnector, ETLDatasource

from pymongo import *

class MongoDatasource(ETLDatasource):
    def __init__(self, data_set_name, db_name, host='localhost', port=27017):
        ETLDatasource.__init__(self, MongoConnector(db_name, host, port), MongoConnector(db_name))
        self.collection = self.input_connector.get_collection(data_set_name)

    def row_count(self):
        return self.collection.count()

    def row_data_set(self):
        for doc in self.collection.find():
            yield doc

class MongoConnector(DataConnector):
    def __init__(self, name, host='localhost', port=27017):
        DataConnector.__init__(self, name)
        self.host = host
        self.port = port
        self.db = None
        self.__data_connection(host, port)

    def get_collection(self, collection):
        return self.db[collection]

    def __data_connection(self, host, port):
        self.db = MongoClient(host, port)[self.name]

