#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BinaryIndexedTree(object):
    def __init__(self, data=None):
        self.tree = None
        self._array = data
        pass

    def _lowbit(self, i):
        return (i & -i)

    def _build(self, data):
        size = len(data)
        for i in range(size):
            j = i + self._lowbit(i+1)
            print "j: %s, i: %s, lowbit: %s" % (j, i, self._lowbit(i+1))
            if j < size:
                data[j] += data[i]

        self._array = data

    def sum(self, i):
        r = 0
        while i:
            r += self._array[i-1]
            i -= self._lowbit(i)
        return r

    def range(self, i, j):
        """
        Returens the sum of elements [i, j-1]
        could be written as sum(a,j) - sum(a, i)
        """
        r = 0
        while j > i:
            r += self._array[j-1]
            j -= self._lowbit(j)

        while i > j:
            r -= self._array[i-1]
            i -= self._lowbit(i)
        return r

    def add(self, i, delta):

        while i < len(self._array):
            self._array[i] += delta
            i += self._lowbit(i+1)

    def get(self, i):
        """
        Returns the value of the element at index i
        """
        return self.range(i, i+1)

    def set(self, i, val):
        self.add(i, val - self.get(i))


if __name__ == '__main__':
    t = BinaryIndexedTree()
    t._build([1,2,3,4,5,6,7,8,9])
    print t.range(2,5)
    print t.get(3)
    print t._array
    t.set(3, 9)
    print t._array
