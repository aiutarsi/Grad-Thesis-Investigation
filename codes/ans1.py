def two_pointers(arr, x):
    if 0 in arr:
        return len(arr)
    res = 0
    sum = 1
    right = 0
    for left in range(len(arr)):
        while right < len(arr) and sum * arr[right] <= x:
            sum *= arr[right]
            right += 1
        res = max(res, right - left)
        if right == left:
            right += 1
        else:
            sum //= arr[left]
    return res


N, K = map(int, input().split())
s = []
for _ in range(N):
    s.append(int(input()))

print(two_pointers(s, K))
