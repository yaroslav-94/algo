t = int(input())
answer = []
for i in range(t):
    _, arr = input(), list(map(int, input().split()))

    if arr == sorted(arr):
        answer.append(0)
    else:
        max_min = 2 * max(arr)
        fl = 0
        while max_min > 0:
            arr_new = [abs(arr[i] - max_min) for i in range(len(arr))]
            if arr_new == sorted(arr_new):
                fl = 1
                answer.append(max_min)
                break
            elif (max(arr_new)) // 2 > 0:
                max_min -= (max(arr_new)) // 2
            else:
                break
        if fl == 0:
            answer.append(-1)

for i in range(t):
    print(answer[i])
