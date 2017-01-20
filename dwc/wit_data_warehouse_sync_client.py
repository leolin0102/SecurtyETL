__author__ = 'lin'

from pymongo import *

class WitDataWarehouseClient:
    def __init__(self):
        self.mongo = None

    def sync_row_data(self, category, collection, data):
        self.mongo = MongoClient()

    def sync_row_data_iter(self, category, collect, data):
        pass

    def fill_data_upload_task(self):
        pass

class RowDataUploadCmd:
    def __init__(self):
        pass
