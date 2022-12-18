def shell_sort(arr):
    h = 1
    while True:
        if 3 * h + 1 <= len(arr):
            h = 3 * h + 1
        else:
            break

    while h > 0:
        for i in range(0, h):
            for j in range(h + i, len(arr), h):
                k = j - h
                tmp = arr[j]
                while tmp < arr[k] and k > -1:
                    arr[k + h] = arr[k]
                    k -= h
                arr[k + h] = tmp
        h //= 3

    return arr


N = int(input())
A = list(map(int, input().split()))

print(*shell_sort(A))
