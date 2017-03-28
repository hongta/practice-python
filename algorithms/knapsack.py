from __future__ import print_function



def knapsack(W, w, v, n):
    F = [[0] * (W+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(W+1):
            # if i == 0:
            #     F[i][j] == 0
            #     break
            if W >= w[i]:
                F[i][j] = max(F[i-1][j], F[i-1][j-w[i]]+v[i])
            else:
                F[i][j] = F[i-1][j]

    return F[n-1][W]

def knapsack2(W, w, v, n):
    F = [0] * (W+1)

    for i in range(n):
        for j in range(W, w[i], -1):
            F[j] = max(F[j-w[i]])

if __name__ == '__main__':
    W = 10
    w = [2,2,6,5,4]
    v = [6,3,5,4,6]
    n = 5
    print knapsack(W, w, v, n)
