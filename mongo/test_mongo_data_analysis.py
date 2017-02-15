__author__ = 'lin'
from pymongo import *
import unittest

from mongo_data_analysis import *

def connect_to_mongo():
    return MongoClient()

class MongoDataAnalysisTestCase(unittest.TestCase):
    def test_get_data_sample(self):
        sample_datas = get_data_sample(connect_to_mongo()['test']['dishes'])
        self.assertIsNotNone(sample_datas)
        self.assertEqual(4, len(sample_datas))


if __name__ == '__main__':
    unittest.main()
