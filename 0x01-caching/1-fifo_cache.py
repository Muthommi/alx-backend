#!/usr/bin/env python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache that firstly removes the oldest items. """
    def __init__(self):
        """ Initializes the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Adds an item using FIFO """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key = self.order.pop(0)
                    del self.cache_data[oldest_key]
                    print(f"DISCARD: {oldest_key}")
                self.cache_data[key] = item
                self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
