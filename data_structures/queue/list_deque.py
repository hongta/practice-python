#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListDeque(object):

    def __init__(self):
        self._items = []

    def __iter__(self):

        for cur in range(len(self._items)):
            yield self._items[cur]

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def enqueue_first(self, item):
        self._items.append(item)

    def enqueue_last(self, item):
        self._items.insert(0, item)

    def dequeue_first(self):
        return self._items.pop()

    def dequeue_last(self):
        return self._items.pop(0)
