def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = arr[left]
    cur_l = left
    cur_r = right
    while True:
        while arr[cur_l] < pivot:
            cur_l += 1
        while arr[cur_r] > pivot:
            cur_r -= 1
        if cur_l >= cur_r:
            break
        arr[cur_l], arr[cur_r] = arr[cur_r], arr[cur_l]
        cur_l += 1
        cur_r -= 1

    quick_sort(arr, left, cur_l - 1)
    quick_sort(arr, cur_r + 1, right)

    return arr


N = int(input())
A = list(map(int, input().split()))

print(*quick_sort(A, 0, len(A) - 1))
