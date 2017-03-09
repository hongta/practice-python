#!/usr/bin/env python
# -*- coding: utf-8 -*-


def quick_sort_dual_pivot(a):
    _quick_sort_dual_pivot(a, 0, len(a) - 1)
    return a

def _quick_sort_dual_pivot(a, lo, hi):

    if lo >= hi:
        return


    if a[lo] > a[hi]:
        a[lo], a[hi] = a[hi], a[lo]

    pivot1 = a[lo]
    pivot2 = a[hi]

    if (pivot1 == pivot2):
        while pivot1 == pivot2 and lo < hi:
            lo +=1
            pivot1 = a[lo]



    l = lo + 1
    h = hi - 1
    i = lo + 1

    while i <= h:
        if a[i] < pivot1:
            a[i], a[l] = a[l], a[i]
            i += 1
            l += 1
        elif a[i] > pivot2:
            a[i], a[h] = a[h], a[i]
            h -= 1
        else:
            i += 1
    l -= 1
    h += 1

    a[lo], a[l] = a[l], a[lo]
    a[hi], a[h] = a[h], a[hi]


    _quick_sort_dual_pivot(a, lo, l-1)
    _quick_sort_dual_pivot(a, l+1, h-1)
    _quick_sort_dual_pivot(a, h+1, hi)


if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99, 12, 12]
    print quick_sort_dual_pivot(d)
