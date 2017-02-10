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


if __name__ == '__main__':
    d = [4,2,1,10,10,5,3,22, 7, 1]

    print counting_sort(d)
