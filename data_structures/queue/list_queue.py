#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListQueue(object):

    def __init__(self):
        self._items = []

    def __iter__(self):
        items = range(len(self._items))

        for cur in items:
            yield self._items[cur]

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

if __name__ == '__main__':
    l = ListQueue()
    l.enqueue(23)
    l.enqueue(12)
    l.enqueue(25)
    l.enqueue(27)
    print l._items
    for v in l:
        print v
