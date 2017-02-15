__author__ = 'lin'
from pymongo import *
def get_data_sample(collection):
    sample_data = []
    for d in collection.find(limit=1000):
        print d
        sample_data.append(d)
    return sample_data
