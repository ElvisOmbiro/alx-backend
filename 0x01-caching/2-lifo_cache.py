#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
"""
Create a class LIFOCache that inherits from BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class implements LIFO cache Algorithm
    """
    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """
        Stores cache data in a dictionary

        Args:
            key(str) - key
            item(str) - item
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                latest_key, latest_item = self.cache_data.popitem()
                print("DISCARD: {}".format(latest_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the data stored in a cache store

        Args:
            key(str)- key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
