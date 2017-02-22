#!/usr/bin/env python
# -*- coding: utf-8 -*-

# References http://stackoverflow.com/questions/18761766/mergesort-python


def merge_sort(a):
    if len(a) == 1:
        return a

    result = []
    mid = len(a) // 2

    lo_a = merge_sort(a[:mid])
    hi_a = merge_sort(a[mid:])

    # merging two part of array
    i = 0
    j = 0
    while i < len(lo_a) and j < len(hi_a) :
        if lo_a[i] < hi_a[j]:
            result.append(lo_a[i])
            i +=1
        else:
            result.append(hi_a[j])
            j +=1
    # merge the rest
    result.extend(lo_a[i:])
    result.extend(hi_a[j:])

    return result

def merge_sort2(a):
    return _merget_sort2(a, 0, len(a))

def _merge_sort2(a, lo, hi):
    if hi - lo > 1:
        mid = lo + (hi - lo) // 2
        _merget_sort2(a, lo, mid)
        _merget_sort2(a, mid, hi)
        _merge2(a, ho, mid, hi)
    return a

def _merge2(a, lo, mid, hi):
    i = 0
    j = mid
    #TODO: will update this function

from heapq import merge

def _merge3(a):
    if len(a) < 2:
        return a
        
    mid = len(a) // 2
    return merge(merge3(a[:mid]), merge3(a[mid:]))

def merge3(a):
    return list(_merge3(a))


if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    #print merge_sort(d)
    print merge3(d)
