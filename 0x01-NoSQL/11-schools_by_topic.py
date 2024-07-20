#!/usr/bin/env python3
"""
This module provides a function that
filter document using specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Filter documents by topic"""
    return list(mongo_collection.find({"topics": topic}))
