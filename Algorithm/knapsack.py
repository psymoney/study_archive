def knapsack(N, K, W, V):
    m = [[0] * (K + 1) for _ in range(N + 1)]
    for n in range(N):
        for k in range(1, K + 1):
            a = 0
            b = m[n-1][k]
            c = 0
            if k >= W[n]:
                a = V[n]
                c = m[n-1][k-W[n]] + V[n]

            m[n][k] = max(a, b, c)


    print(m)
    return m[N - 1][K]

print(knapsack(4, 20, [5,7,12,18], [13,8,6,12]))

N, K = input().split()
N,K = int(N), int(K)
W = [None] * N
V = [None] * N

for i in range(N):
    w, v = input().split()
    W[i] = int(w)
    V[i] = int(v)

print(N, K, W, V)