#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
    for i in range(1, len(a)):
        current_val = a[i]
        j = i
        while j > 0 and a[i-1] > current_val:
            a[j] = a[i-1]
            j -= 1
        a[j] = current_val
    return a

if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print insertion_sort(d)
    e = [3, 2]
    print insertion_sort(e)
