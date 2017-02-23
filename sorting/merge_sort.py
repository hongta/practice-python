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
    _merge_sort2(a, 0, len(a)-1)
    return a

def _merge_sort2(a, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    _merge_sort2(a, lo, mid)
    _merge_sort2(a, mid+1, hi)
    _merge(a, lo, mid, hi)


def _merge2(a, lo, mid, hi):
    i = 0
    j = mid
    #TODO: will update this function

from heapq import merge

def _merge_sort3(a):
    if len(a) < 2:
        return a

    mid = len(a) // 2
    return merge(merge3(a[:mid]), merge3(a[mid:]))

def merge_sort3(a):
    return list(_merge_sort3(a))

def _merge(a, lo, mid, hi):
    i = lo
    j = mid + 1
    aux = a[:]
    print lo,mid,hi
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j+=1
        elif j > hi+1:
            a[k] = aux[i]
            i +=1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j+=1
        else:
            a[k] = aux[i]
            i+=1

def merge_sort4(a):
    N = len(a)
    sz = 1
    for sz in range(1, N, sz+sz):
        print sz
        for lo in range(0,N-sz, sz+sz):
            print lo
            _merge(a, lo, lo+sz-1, min(lo+sz+sz-1,N-1))

    return a



if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    #print merge_sort(d)
    print merge_sort2(d)
