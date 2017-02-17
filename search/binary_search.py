#!/usr/bin/env python
# -*- coding: utf-8 -*-

def binary_search(a, needle):

    def _binary_search(lo, hi):
        print lo, hi
        mid = lo + (hi - lo) //2
        if lo > hi:
            return False
        elif a[mid] < needle:
            return _binary_search(mid + 1, hi)
        elif a[mid] > needle:
            return _binary_search(lo, mid - 1)
        else:
            return mid

    return _binary_search(0, len(a)-1)

if __name__ == '__main__':
    d = sorted([2,3,6, 21, 23,5, 10,30,24, 15])
    print d
    print binary_search(d, 10)
