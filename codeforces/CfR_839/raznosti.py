t = int(input())
answer = []
for i in range(t):
    k, n = map(int, input().split())
    arr = [1]
    for i in range(1, k):
        arr.append(arr[-1] + i)
    if arr[-1] > n:
        for i in range(k):
            if n - arr[i] < len(arr) - i - 1:
                arr[i] = arr[i - 1] + 1
    answer.append(' '.join(str(i) for i in arr))

for i in range(t):
    print(answer[i])
