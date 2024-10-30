#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Caching system to discard most recently used items first """

    def __init__(self):
        """ Function to initialize cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Function to add an item to the cache using MRU """
        if key is None and item is None:
            return

            if key in self.cache_data:
                self.cache_data.pop(key)

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item

    def get(self, key):
        """ Gets an item by key """
        if key is None or key not in  self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
