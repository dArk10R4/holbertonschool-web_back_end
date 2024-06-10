#!/usr/bin/env python3
""" Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """Function that inserts document to NoSQL"""
    return mongo_collection.insert({**kwargs})
