MAX = int(1e5)


def eratosthenes(N):
    is_prime = [True for _ in range(N + 1)]
    is_prime[0] = is_prime[1] = False
    i = 2
    while i * i <= N:
        if is_prime[i]:
            j = i * 2
            while j <= N:
                is_prime[j] = False
                j += i
        i += 1
    return is_prime


is_prime = eratosthenes(MAX)
cumulative_sum = [0 for _ in range(MAX + 1)]
for i in range(1, MAX + 1):
    cumulative_sum[i] += cumulative_sum[i - 1]
    if i % 2 and is_prime[i] and is_prime[(i + 1) // 2]:
        cumulative_sum[i] += 1

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(cumulative_sum[r] - cumulative_sum[l - 1])
