#!/usr/bin/env python
# -*- coding: utf-8 -*



def heap_sort(a):

    #sift up ????
    def sink_max(k, N):
        n = N-1
        while 2*k+1 <= n:
            c = 2*k+1
            if c < n and a[c] < a[c+1]:
                c+=1

            if a[k] > a[c]:
                break
            a[k], a[c] = a[c], a[k]

            k = c
    N = len(a)
    # build max heap using bottom-up method
    for i in reversed(xrange(N//2)):
        sink_max(i, N)

    while N > 1:
        N = N-1
        a[0], a[N], = a[N], a[0]
        sink_max(0, N)

    return a

if __name__ == '__main__':
    d = [34,2,24,12, 45,33,9,99]
    print heap_sort(d)
