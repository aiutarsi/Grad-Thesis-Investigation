def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left_arr = merge_sort(arr[: len(arr) // 2])
    right_arr = merge_sort(arr[len(arr) // 2 :])

    mem = []
    cur_l = cur_r = 0
    while cur_l < len(left_arr) and cur_r < len(right_arr):
        if left_arr[cur_l] <= right_arr[cur_r]:
            mem.append(left_arr[cur_l])
            cur_l += 1
        else:
            mem.append(right_arr[cur_r])
            cur_r += 1

    if cur_l < len(left_arr):
        mem += left_arr[cur_l:]
    if cur_r < len(right_arr):
        mem += right_arr[cur_r:]

    return mem


N = int(input())
A = list(map(int, input().split()))

print(*merge_sort(A))
