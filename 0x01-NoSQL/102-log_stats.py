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


def get_top_ips(nginx_collection):
    """
    Get top ips in documents (group and aggregate)
    Returns cursor object
    """
    return nginx_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "requests": {"$sum": 1}
            }
        },
        {"$sort": {'requests': -1}},
        {"$limit": 10}
    ])


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
    top_ips = get_top_ips(nginx_collection)
    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip["_id"], ip["requests"]))


if __name__ == "__main__":
    main()
