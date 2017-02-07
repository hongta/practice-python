
def shell_sort(a):
    "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
    gap = len(a) // 2
    # loop over the gaps
    while gap > 0:
        #do the insertion sort
        for i in range(gap, len(a)):
            val = a[i]
            j = i
            while j >= gap and a[j - gap] > val:
                a[j] = a[j - gap]
                j -= gap
            a[j] = val
        gap //= 2

    return a

if __name__ == '__main__':
    v = [3,21,8,1,90,23,19,57,24]
    print v
    print shell_sort(v)
