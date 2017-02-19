#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
    for i in range(1, len(a)):
        current_val = a[i]
        j = i
        while j > 0 and a[j-1] > current_val:
            a[j] = a[j-1]
            j -= 1
        a[j] = current_val
    return a

def insertion_sort2(a):
    for i in range(0, len(a)):
        for j in reversed(range(1, i+1)):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
            else:
                break
    return a

def insertion_sort3(a):
    for i in range(0, len(a)):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            j-=1
    return a

if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print insertion_sort3(d)
    e = [2, 3]
    print insertion_sort3(e)
