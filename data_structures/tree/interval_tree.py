#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import IntervalTreeNode

class IntervalTree(object):
    def __init__(self):
        self.root = None

    def insert(self, interval):
        self.root = self._insert(self.root, interval)

    def _insert(self, node, interval):

        if not node:
            node = IntervalTreeNode()
            (node.low, node.high) = interval
            node.max = interval[1]
            return node

        low = node.low
        if interval[0] < low:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)

        if node.max < interval[1]:
            node.max = interval[1]

        return node

    def is_overlap(self, interval_1, interval_2):
        if interval_1[0] <= interval_2[1] and interval_2[0] <=interval_1[1]:
            return True
        return False

    def search(self, interval):
        return self._search(self.root, interval)

    def _search(self, node, interval):

        if not node:
            return None

        print "is overlaps", self.is_overlap((node.low, node.high), interval)
        if self.is_overlap((node.low, node.high), interval):
            return (node.low, node.high)

        if node.left and node.left.max >= interval[0]:
            return self._search(node.left, interval)

        return self._search(node.right, interval)


if __name__ == '__main__':
    t = IntervalTree()
    t.insert((5,12))
    t.insert((4,8))
    t.insert((10,15))
    print t.root
    print t.search((13,15))
