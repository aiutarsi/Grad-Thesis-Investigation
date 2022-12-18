def is_ok(index, key, arr):
    return True if arr[index] >= key else False


def binary_search(key, arr):
    ng = -1
    ok = len(S)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if arr[mid] == key:
            return True
        elif is_ok(mid, key, arr):
            ok = mid
        else:
            ng = mid
    return False


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for t in T:
    if binary_search(t, S):
        ans += 1

print(ans)
