MAX = 10001


def count_sort(arr):
    count = [0 for _ in range(MAX)]
    for i in arr:
        count[i] += 1

    index = 0
    for i in range(0, MAX):
        for _ in range(count[i]):
            arr[index] = i
            index += 1

    return arr


N = int(input())
A = list(map(int, input().split()))

print(*count_sort(A))
