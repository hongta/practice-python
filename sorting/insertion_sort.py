#!/usr/bin/env python
# -*- coding: utf-8 -*-


def insertion_sort(a):

    for i in range(len(a)):
        for j in reversed(range(1, i)):
            if a[j-1] > a[j]:
                a[j],a[j-1] = a[j-1],a[j]
            else:
                break
    return a

if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print insertion_sort(d)
