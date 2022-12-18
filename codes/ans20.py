def shaker_sort(arr):
    left = 0
    right = len(arr) - 1
    while right > left:
        last = -1
        i = left
        while i < right:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last = i
            i += 1
        i = right = last
        while i > left:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                last = i
            i -= 1
        left = last
    return arr


N = int(input())
A = list(map(int, input().split()))

print(*shaker_sort(A))
