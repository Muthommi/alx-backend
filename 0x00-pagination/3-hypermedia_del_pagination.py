#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.
"""


import csv
from typing import List, Dict


class Server:
    """
    Server class to paginate the database of popolar baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion resilient hypermedia pagination.
        """
        assert index is not None and 0 <= index < len(self.indexed_dataset())

        data = []
        current_index = index
        indexed_data = self.indexed_dataset()

        while len(data) < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = (
            current_index if current_index < len(self.dataset()) else None)

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }