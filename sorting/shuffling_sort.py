
from random import randint

def shuffling_sort(a):
    for i in range(len(a)):
        r = randint(0,i)
        a[i],a[r] = a[r],a[i]

    return a

if __name__ == '__main__':
    v = [3,21,8,1,90,23,19,57,24]
    print v
    print shuffling_sort(v)
