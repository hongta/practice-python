#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import IntervalTreeNode

class IntervalTree(object):
    def __init__(self):
        self.root = None

    def insert(self, interval):
        if not self.root:
            t.low = interval[0]
            t.high = interval[1]
            self.root = t
            return
            
        self._insert(self.root, interval)

    def _insert(self, node, interval):

        low = node.low

        if interval[0] < low:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)

        if node.max < interval[1]:
            node.max = interval[1]

        return node
