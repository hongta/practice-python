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
            raise IndexError("index out of bounds")

        self._update_value(0, len(self.orignal_data)-1, 0, index, value)

    def _update_value(self, in_start, in_end, node, index, value):
        if index < in_start or index > in_end:
            return

        if in_start == in_end:
            self.t[node] = value
            return

        mid = in_start + (in_end - in_start) // 2
        self._update_value(in_start, mid, 2*node+1, index, value)
        self._update_value(mid+1, in_end, 2*node+2, index, value)

        self.t[node] = self.t[node*2] + self.t[node*2+1]


    def _build(self, node , in_start, in_end):

        if in_start == in_end:
            self.t[node] = self.orignal_data[in_start]
            return self.t[node]

        mid = in_start + (in_end - in_start) // 2
        self.t[node] = (self._build(2*node+1, in_start, mid)
                        + self._build(2*node+2, mid+1, in_end))

        return self.t[node]

    def query_sum(self, qs, qe):
        if qs < 0 or qe > len(self.orignal_data) - 1 or qs > qe:
            raise IndexError("index out of bounds")

        return self._query_sum(0, qs, qe, 0, len(self.orignal_data)-1)

    def _query_sum(self, node, qs, qe, in_start, in_end):

        # if segment of this node is a port of given range, then return node data
        if qs <= in_start and qe >= in_end:
            return self.t[node]

        #outside of given range
        if in_end < qs or in_start > qe:
            return 0

        mid = in_start + (in_end - in_start) // 2
        return (self._query_sum(2*node+1, qs, qe, in_start, mid)
                + self._query_sum(2*node+2, qs, qe, mid+1, in_end))

if __name__ == '__main__':
    s = SegmentTree([1,2,3,4,5,6,7,8])
    print s.t
    # s.update_value(0,9)
    # print s.t
    # print len(s.t)
    print s.query_sum(1,3)
