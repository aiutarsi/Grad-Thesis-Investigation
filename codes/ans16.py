def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        tmp = arr[i]
        while arr[j] > tmp and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    return arr


N = int(input())
A = list(map(int, input().split()))

print(*insertion_sort(A))
