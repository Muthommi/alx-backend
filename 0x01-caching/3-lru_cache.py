#!/usr/bin/env python3
""" LRUCache module """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Caching system that discards recently used items first """
    def __init__(self):
        """ Initializes the cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Adds an item to the cache using LRU """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Function to get an item by key """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
