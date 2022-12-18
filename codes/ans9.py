MOD = int(1e9 + 7)


def power_mod(a, p):
    if p == 0:
        return 1
    tmp = power_mod(a * a % MOD, p // 2)
    if p % 2:
        tmp = tmp * a % MOD
    return tmp


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % MOD
    return res


def combination(n, k):
    return factorial(n) * power_mod(factorial(n - k), MOD - 2) * power_mod(factorial(k), MOD - 2) % MOD


W, H = map(int, input().split())
print(combination(W + H - 2, W - 1))
