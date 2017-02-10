#!/usr/bin/env python
# -*- coding: utf-8 -*


def counting_sort(a):
    return _counting_sort(a, max(a))

def _counting_sort(a, max_value):
    """
    sorting positive integers less than or equal to max_value
    """
    result = []
    counter = [0] * (max_value + 1)

    for i in a:
        counter[i] += 1

    for i, count in enumerate(counter):
        result.extend([i]* count)

    return result


def counting_sort_in_place(a):
    """
    in-place counting sort
    http://p-nand-q.com/python/algorithms/sorting/countingsort.html
    """

    counter = [0] * (max(a) + 1)
    for i in a:
        counter[i] += 1

    pos = 0
    for i, count in enumerate(counter):
        for _ in range(count):
            a[pos] = i
            pos += 1

    return a

if __name__ == '__main__':
    d = [4,2,1,10,10,5,3,22, 7, 1]
    print counting_sort_in_place(d)
    print counting_sort(d)
