#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WeightedQuickUnion(object):

    def __init__(self, data=None):
        self.id = data
        self.weight = [1] * len(data)
        self.count = len(data)

    def count(self):
        return self.count

    def find(self, val):
        n = val
        while self.id[n] != n:
            #path compression
            self.id[n] = self.id[self.id[n]]
            n = self.id[n]

        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.weight[p_root] > self.weight[q_root]:
            self.id[q_root] = p_root
            self.weight[q_root] += self.weight[p_root]
        else:
            self.id[p_root] = q_root
            self.weight[p_root] += self.weight[q_root]

        self.count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
