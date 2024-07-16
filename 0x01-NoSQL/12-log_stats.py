"""
This module provies a functions that parses
data in mongodb documents
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_counts(nginx_collection):
    return nginx_collection.count_documents()


def filter_attribute(nginx_collection, method, **kwargs):
    return nginx_collection.find({"method": method, **kwargs})


def main():
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    all_docs = get_counts(nginx_collection)

    print("{} logs\n".format(all_docs))
    print("Methods:\n")
    for method in METHODS:
        print("\tmethod {}: {}\n".format(
            method, filter_attribute(nginx_collection, method)))
    print("{} status check".format(
        filter_attribute(nginx_collection, "GET", path="/status")))
