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

if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print merge_sort(d)
