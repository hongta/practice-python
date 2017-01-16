#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SegmentTree(object):
    def __init__(self, data=None):
        self.t = data
        self.sum_value = {}


    def _build(self, start, end):

        self.sum_value[(start, end)] = 0

        if start < end:
            mid = start + (end - start) // 2
            self._build(start, mid)
            self._build(mid+1, end)

    def _query_sum(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.sum_value[{start, end}]
        else:
            mid = in_start + (in_end - in_start) // 2
            if mid >= end:
                ans = self._query_sum(start, end, in_start, mid)
            elif mid + 1 <= start:
                ans = self._query_sum(start, end, mid+1, end)
            else:
                ans = self._query_sum(start, end, in_start, mid) + self._query_sum(mid+1, end, mid+1, end)

        return ans

if __name__ == '__main__':
    s = SegmentTree()
