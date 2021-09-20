n = int(input())
arr = list(map(int, input().split()))

answer = max(arr)
sum_max = arr[0]
for i in range(1, len(arr)):
    sum_max += arr[i]
    if sum_max > answer:
        answer = sum_max
    elif sum_max < 0:
        sum_max = arr[i]
print(str(answer))
