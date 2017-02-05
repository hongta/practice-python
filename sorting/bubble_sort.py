#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubble_sort(a):

    for i in range(len(a)):
        for j in  reversed(range(i+1, len(a))):
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1], a[j]
    return a

if __name__ == '__main__':
    a = [4,2,1,10,5,3,100]
    print bubble_sort(a)
