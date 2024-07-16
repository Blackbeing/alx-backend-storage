#!/usr/bin/env python3
"""
This module provies a functions that parses
data in mongodb documents
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_counts(nginx_collection):
    """
    Get number of documents in collection
    Return int
    """
    return nginx_collection.count_documents({})


def filter_attribute(nginx_collection, method, **kwargs):
    """
    Filter documents by attribute
    Returns list
    """
    return list(nginx_collection.find({"method": method, **kwargs}))


def main():
    """
    Run main program
    Returns None
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    all_docs = get_counts(nginx_collection)

    print("{} logs".format(all_docs))
    print("Methods:")
    for method in METHODS:
        print("\tmethod {}: {}".format(
            method, len(filter_attribute(nginx_collection, method))))
    print("{} status check".format(
        len(filter_attribute(nginx_collection, method="GET", path="/status"))))


if __name__ == "__main__":
    main()
