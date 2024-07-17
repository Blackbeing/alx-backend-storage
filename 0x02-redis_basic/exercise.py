#!/usr/bin/env python3
"""
This module provides a class to interface with
redis server via python
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    Initialize redis server and delete all keys in db
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Add random key with value in redis database
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
