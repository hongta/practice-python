#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class SegmentTree(object):
    def __init__(self, data=None):
        height = int(math.ceil(math.log(len(data))/math.log(2)))
        self.max_size = 2 * int(math.pow(2, height)) - 1

        self.tree = [None] * self.max_size
        self._array = data

        self._build(0, 0, len(data)-1)


    def _build(self, node , a, b):

        # 1. update leaf node data
        if a == b:
            self.tree[node] = self._array[a]
            return self.tree[node]

        # 2. build left child in range [a, (a+b)/2]
        #      and right child in range [(a+b)/2+1, b]
        mid = a + (b - a) // 2
        self.tree[node] = (self._build(2*node+1, a, mid)
                        + self._build(2*node+2, mid+1, b))

        return self.tree[node]

    def update_value(self, index, value):
        if index not in range(len(self._array)):
            raise IndexError("index out of bounds")

        self._update_value(0, 0, len(self._array)-1, index, value)

    def _update_value(self, node, a, b, index, value):

        # 1. index outside the range of this segment
        if index < a or index > b:
            return

        # 2. the leaf node we want to update
        if a == b:
            self.tree[node] = value
            return

        # 3. update left child in range [a, (a+b)/2]
        #      and right child in range [(a+b)/2+1, b]
        mid = a + (b - a) // 2
        self._update_value(2*node+1, a, mid, index, value)
        self._update_value(2*node+2, mid+1, b, index, value)

        # 4. update node data after children.
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def query_sum(self, i, j):
        if i < 0 or j > len(self._array) - 1 or i > j:
            raise IndexError("index out of bounds")

        return self._query_sum(0, 0, len(self._array)-1, i, j)

    def _query_sum(self, node, a, b, i, j):

        # 1. outside of given range
        if b < i or a > j:
            return 0

        # 2. if segment of this node is a port of given range, then return node data
        if i <= a and j >= b:
            return self.tree[node]


        # 3. If a part of this segment [a, b] overlaps with the given range [i, j]
        mid = a + (b - a) // 2
        return (self._query_sum(2*node+1, a, mid, i, j)
                + self._query_sum(2*node+2, mid+1, b, i, j))

class SegmentTreeLazy(SegmentTree):
    def __init__(self, data=None):
        super(SegmentTreeLazy, self).__init__(data)

        self.lazy = [0] * self.max_size

    def update_range_value(self, i, j, value):
        if (i not in range(len(self._array))
            or j not in range(len(self._array))):
            raise IndexError("index out of bounds")

        self._update_range_value(0, 0, len(self._array) -1, i, j, value)

    def _update_range_value(self, node, a, b, i, j, value):

        print node, a, b
        if self.lazy[node] != 0:
            print "update from lazy"
            self.tree[node] += (b - a + 1) * self.lazy[node]

            if a != b: # not leaf node
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+1] += self.lazy[node]

            self.lazy[node] = 0

        # segment [a, b] are outside of given range  [i, j]
        if b < i or a > j:
            return

        # segment [a, b] is a port of given range [i, j]
        if i <=a and j >=b:
            print "in range (%s, %s)" % (a, b)
            self.tree[node] += (b - a + 1) * value

            if a != b:
                print "update lazy"
                self.lazy[2*node+1] += value
                self.lazy[2*node+2] += value

            return
        # segment [a, b] overlaps given range [i, j]
        mid = a + (b - a)/2
        self._update_range_value(2*node+1, a, mid, i, j, value)
        self._update_range_value(2*node+2, mid+1, b, i, j, value)

        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

if __name__ == '__main__':
    s = SegmentTree([1,2,3,4,5,6,7,8])
    print s.tree
    #s.update_value(0,9)
    #print s.tree
    # print len(s.tree)
    print s.query_sum(1,3)
