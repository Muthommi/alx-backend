#!/usr/bin/env python3
""" Basic cache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system with no size limit """
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
