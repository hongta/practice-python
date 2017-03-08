#!/usr/bin/env python
# -*- coding: utf-8 -*-


def quick_sort_3way(a):
    _quick_sort_3way(a, 0, len(a) - 1)
    return a

def _quick_sort_3way(a, lo, hi):

    if lo >= hi:
        return

    l = lo
    h = hi
    i = l + 1
    pivot = a[lo]

    while i <= h:
        if a[i] < pivot:
            a[i], a[l] = a[l], a[i]
            i += 1
            l += 1
        elif a[i] > pivot:
            a[i], a[h] = a[h], a[i]
            h -= 1
        else:
            i += 1

    _quick_sort_3way(a, lo, l-1)
    _quick_sort_3way(a, h+1, hi)


if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print quick_sort_3way(d)
