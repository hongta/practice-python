#!/usr/bin/env python
# -*- coding: utf-8 -*-
from insertion_sort import insertion_sort

def bucket_sort(a):
    """
        0.0 <= a[i] <= 1
    """
    b = [[] for _ in a]
    n = len(a)
    for v in a:
        b[int(n*v)].append(v)
    a = []
    for i in range(len(b)):
        a.extend(insertion_sort(b[i]))
        
    return a
if __name__ == '__main__':
    d=[0.7, 0.23, 0.03, 0.92,0.21]
    bucket_sort(d)
