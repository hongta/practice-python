#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MinBinaryHeap(object):
    def __init__(self):
        self._heap = [0]
        self._size = 0

    def insert(self, v):
        self._heap.append(v);
        self._size+=1
        self._sift_up(len(self._heap) - 1)

    def extract_min(self):
        self._exchange(1, len(self._heap) - 1)
        del self._heap[-1]
        self._sift_down(1)

    def get_min(self):
        self._heap[1];

    def size(self):
        return len(self._heap) - 1

    def _sift_up(self, p):
        while p > 1 and self._less(p, p/2):
            self._exchange(p, p/2)
            p = p/2

    def _sift_down(self, p):

        while 2*p <= (len(self._heap)-1):

            # 2*p is the left child of p
            # 2*p+1 is the right child of p
            c = 2 * p
            if c < (len(self._heap)-1) and not self._less(c, c+1):
                c +=1

            if self._less(p, c):
                break

            self._exchange(p, c)
            p = c


    def _less(self, p, q):
        return self._heap[p] < self._heap[q]

    def _exchange(self, p, q):
        self._heap[p], self._heap[q] = self._heap[q], self._heap[p]
