__author__ = 'lin'

class ETLDatasource:
    def __init__(self, input_connector, output_connector, meta_data_filter=None):
        self.input_connector = input_connector
        self.output_connector = output_connector
        self.meta_data_filter = meta_data_filter

    def sync_data(self):
        pass

    def row_count(self):
        pass

    def close(self):
        pass

    def row_data_set(self):
        pass

class DataConnector:
    def __init__(self, name):
        self.name = name

    def connection(self):
        pass

