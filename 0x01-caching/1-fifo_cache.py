#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system:
"""
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO algorithm class implementation
    """
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        Stores items in cache dictionary

        Args:
            key(str) - key
            item(str) - item
        """
        if key and item:
            self.cache_data[key] = item
            self.queue.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.popleft()
                self.cache_data.pop(oldest_key)
                print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """
        Retrieves items from cache store

        Args:
            key(str) -key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
