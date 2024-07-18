#!/usr/bin/env python3
"""
This module provides a class to interface with
redis server via python
"""
import uuid
from typing import Callable, Optional, Union

import redis


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

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, int, bytes, float]:
        raw_value = self._redis.get(key)
        if fn is None:
            return raw_value
        return fn(raw_value)

    def get_str(self, key: str) -> Union[str, int, bytes, float]:
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Union[str, int, bytes, float]:
        return self.get(key, int)
