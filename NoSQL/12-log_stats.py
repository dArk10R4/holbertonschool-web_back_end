#!/usr/bin/env python3
""" Log Stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{logs_collection.count_documents({})} logs\nMethods:")
    for method in methods:
        print("\tmethod {}: {}".
              format(method,
                     logs_collection.count_documents({"method": method})))
    print("{} status check".format(logs_collection.
          count_documents({"method": 'GET', "path": "/status"})))
