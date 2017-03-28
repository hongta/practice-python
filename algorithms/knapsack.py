from __future__ import print_function



def knapsack(W, w, v, n):
    F = [[0] * (W+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(W+1):
            if j >= w[i]:
                F[i][j] = max(F[i-1][j], F[i-1][j-w[i]]+v[i])
            else:
                F[i][j] = F[i-1][j]

    return F[n-1][W]

def knapsack2(W, w, v, n):
    F = [0] * (W+1)

    for i in range(n):
        for j in range(W, w[i], -1):
            F[j] = max(F[j-w[i]] + v[i], F[j])
    return F[-1]

if __name__ == '__main__':
    W = 16
    w = [4,5,10,3]
    v = [30,20,40,10]
    n = 4
    print(knapsack(W, w, v, n))
    print(knapsack2(W, w, v, n))
