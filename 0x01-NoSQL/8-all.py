#!/usr/bin/env python3
"""
This module provides function to list all
documents in collection in mongodb using pymongo
"""


def list_all(mongo_collection):
    """List all documents in collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
