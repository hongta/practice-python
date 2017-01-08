#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack(object):

    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return not self._items

    def push(self, data):
        self._items.append(data)

    def pop(self):
        if self.is_empty():
            return None

        v = self._items[-1]
        del self._items[-1]
        return v

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
