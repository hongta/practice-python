#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class SegmentTree(object):
    def __init__(self, data=None):
        height = int(math.ceil(math.log(len(data))/math.log(2)))
        self.max_size = 2 * int(math.pow(2, height)) - 1
        self.t = [None] * self.max_size
        self.orignal_data = data

        self._build(0, 0, len(data)-1)

    def update_value(self, index, value):
        if index not in range(len(self.orignal_data)):
            return
        diff = value - self.orignal_data[index]
        self._update_value(0, len(self.orignal_data)-1, 0, index, value)

    def _update_value(self, start, end, node, index, value):
        if index < start or index > end:
            return

        if start == end:
            self.t[node] = value
            return

        mid = start + (end - start) // 2
        self._update_value(start, mid, 2*node+1, index, value)
        self._update_value(mid+1, end, 2*node+2, index, value)

        self.t[node] = self.t[node*2] + self.t[node*2+1]


    def _build(self, index, start, end):

        if start == end:
            self.t[index] = self.orignal_data[start]
            return self.t[index]

        if start < end:
            mid = start + (end - start) // 2
            self.t[index] = (self._build(2*index+1, start, mid)
                            + self._build(2*index+2, mid+1, end))

        return self.t[index]

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
    s = SegmentTree([1,2,3,4,5,6,7,8])
    print s.t
    s.update_value(0,9)
    print s.t
    print len(s.t)
