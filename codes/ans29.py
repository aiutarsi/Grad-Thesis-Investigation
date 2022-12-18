N, W = map(int, input().split())
v = [0 for _ in range(N)]
w = [0 for _ in range(N)]
for i in range(N):
    v[i], w[i] = map(int, input().split())

dp = [[float("inf") for _ in range(10001)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 0

for i in range(N):
    for j in range(10001):
        dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i]) if j - v[i] >= 0 else dp[i][j]

for i in reversed(range(10001)):
    if dp[N][i] <= W:
        print(i)
        break
