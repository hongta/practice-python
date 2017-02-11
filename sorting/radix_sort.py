#!/usr/bin/env python
# -*- coding: utf-8 -*-



def radix_sort(a, n, digit_length):

    for x in range(digit_length):
        bins = [[] for i in range(n)]
        for y in a:
            bins[(y/10**x)%n].append(y)

        a = []
        for section in bins:
            a.extend(section)
    return a

if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print radix_sort(d, 10, 2)
