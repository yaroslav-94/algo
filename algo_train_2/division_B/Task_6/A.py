n = int(input())
arr = sorted(list(map(int, input().split())))
k = int(input())


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


answer = []
for i in range(k):
    left, right = map(int, input().split())
    idx_l = left_search(l=0, r=len(arr) - 1, arr=arr, left=left)
    idx_r = rigth_search(l=0, r=len(arr) - 1, arr=arr, right=right)
    if arr[idx_r] < left or arr[idx_l] > right:
        answer.append(0)
    else:
        answer.append(idx_r-idx_l+1)

print(*answer)
