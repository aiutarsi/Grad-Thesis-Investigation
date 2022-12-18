N, W = map(int, input().split())
v = [0 for _ in range(N)]
w = [0 for _ in range(N)]
for i in range(N):
    v[i], w[i] = map(int, input().split())

dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(W + 1):
        dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i]) if j - w[i] >= 0 else dp[i][j]

print(dp[N][W])
