#!/usr/bin/env python3
""" LFU Cache module """

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ Caching system that discards lest frequently used items """
    def __init__(self):
        """ Function to initialize the cache """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = {}

    def put(self, key, item):
        """ Function to add an item to the cache """
        if key is not None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item

        if key in self.usage_frequency:
            self.usage_frequency[key] += 1
        else:
            self.usage_frequency[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_key = min(
                self.usage_frequency,
                key=lambda k: (
                    self.usage_frequency[k],
                    list(self.cache_data).index(k)
                )
            )
            self.cache_data.pop(lfu_key)
            self.usage_frequency.pop(lfu_key)
            print(f"DISCARD: {lfu_key}")

    def get(self, key):
        """ Get an item by key and update the frequency """
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
