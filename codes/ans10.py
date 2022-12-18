s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
for i in range(len(s1)):
    dp[i + 1][0] = i + 1
for i in range(len(s2)):
    dp[0][i + 1] = i + 1

for i in range(len(s1)):
    for j in range(len(s2)):
        dp[i + 1][j + 1] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i][j]) if s1[i] == s2[j] else min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i][j] + 1)

print(dp[len(s1)][len(s2)])
