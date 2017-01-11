#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class RandomizedQueue(object):
    def __init__(self):
        self._items = []

    def __iter__(self):
        items = range(len(self._items))
        random.shuffle(items)

        for cur in items:
            yield self._items[cur]

    def is_empty(self):
        return self.size() == 0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self._items)

    def enqueue(self, item):
        if not item:
            raise ValueError("Invalid item value")

        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("the queue is empty.")

        index = random.randint(0, len(self._items)-1)
        item = self._items[index]

        self._items[index] = self._items[-1]
        del self._items[-1]

        return item

    def sample(self):
        if self.is_empty():
            raise ValueError("the queue is empty.")

        return random.choice(self._items)
