def knapsack(N, K, W, V):
    m = [[0] * (K + 1) for _ in range(N + 1)]
    for n in range(N):
        for k in range(1, K + 1):
            if W[n] <= k:
                m[n][k] = V[n]
            if m[n - 1][k] > m[n][k]:
                m[n][k] = m[n - 1][k]
            if m[n - 1][K-W[n]] + V[n] > m[n][k]:
                m[n][k] = m[n - 1][K-W[n]] + V[n]

    print(m)
    return m[N - 1][K]

print(knapsack(4, 7, [6,4,3,5], [13,8,6,12]))

N, K = input().split()
N,K = int(N), int(K)
W = [None] * N
V = [None] * N

for i in range(N):
    w, v = input().split()
    W[i] = int(w)
    V[i] = int(v)

print(N, K, W, V)