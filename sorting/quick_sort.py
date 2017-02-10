#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quick_sort(a):
    _quick_sort(a, 0, len(a)-1)
    return a


def _quick_sort(a, lo, hi):

    if lo < hi:
        j = partition(a, lo, hi)
        _quick_sort(a, lo, j-1)
        _quick_sort(a, j+1, hi)

def partition(a, lo, hi):

    # simply select first element as pivot
    #   or use sorted(low, midum, high)[1] as pivot,
    #       and exchange with a[lo]
    pivot = a[lo]

    border = lo
    for i in range(lo, hi + 1):
        if a[i] < pivot:
            border +=1
            a[i], a[border] = a[border], a[i]
    a[lo], a[border] = a[border], a[lo]

    return border

if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print quick_sort(d)
