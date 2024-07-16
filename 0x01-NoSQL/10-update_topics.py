#!/usr/bin/env python3
"""
This module provides function to update
multiple documents
"""


def update_topics(mongo_collection, name, topics):
    """ Update documents topics"""
    return mongo_collection.update_many(
        {name: name},
        {"$set": {"topics": topics}}
    )
