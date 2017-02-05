#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(a):
    for i in range(len(a)):
        mini = i
        for j in range(i+1, len(a)):
            if a[mini] > a[j]:
                mini = j
        a[mini], a[i] = a[i], a[mini]

    return a


if __name__ == '__main__':
    a = [4,2,1,10,5,3,100]
    print selection_sort(a)
