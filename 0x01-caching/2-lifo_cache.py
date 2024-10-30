#!/usr/bin/env python3
""" This module handles LIFO cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system that removes most recent items first """

    def __init__(self):
        """ Function to initialize the cache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Adds an item to cache using LIFO """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Gets an item by key """
        return self.cache_data.get(key, None)
