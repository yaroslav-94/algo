n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr_find = list(map(int, input().split()))


def left_search(l, r, arr, left):
    while l < r:
        m = (l + r) // 2
        if arr[m] >= left:
            r = m
        else:
            l = m + 1
    return l


def rigth_search(l, r, arr, right):
    while l < r:
        m = (l + r + 1) // 2
        if arr[m] <= right:
            l = m
        else:
            r = m - 1
    return l


for i in range(k):
    idx_l = left_search(l=0, r=len(arr) - 1, arr=arr, left=arr_find[i])
    idx_r = rigth_search(l=0, r=len(arr) - 1, arr=arr, right=arr_find[i])
    if arr[idx_l] != arr_find[i] and arr[idx_r] != arr_find[i]:
        print(0, 0)
    else:
        print(idx_l+1, idx_r+1)
