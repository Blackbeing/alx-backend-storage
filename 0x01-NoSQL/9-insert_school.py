#!/usr/bin/env python3
"""
This module provides a function that inserts new
document in collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert new document
    Returns: new Object id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
