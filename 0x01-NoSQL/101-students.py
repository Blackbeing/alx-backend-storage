#!/usr/bin/env python3

"""
Module provides a function that
returns sorted documents from collection in mongodb
"""


def top_students(mongo_collection):
    """Sort documents by attribute"""
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
