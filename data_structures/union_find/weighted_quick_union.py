#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WeightedQuickUnion(object):

    def __init__(self):
        self.id = []
        self.weight = []

    def find(self, val):
        p = val
        while self.id[p] != p:
            p = self.id[p]

        return self.id[p]

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        self.id[q_root] = p_root

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
