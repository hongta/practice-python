#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import IntervalTreeNode

class IntervalTree(object):
    def __init__(self):
        self.root = None

    def insert(self, interval):
        self._insert(self.root, interval)

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

if __name__ == '__main__':
    t = IntervalTree()
    t.insert((5,12))
    t.insert((4,8))
    t.insert((10,15))
    
