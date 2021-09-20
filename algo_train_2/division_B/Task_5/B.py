n = int(input())
arr = list(map(int, input().split()))

arr_pref = [0 for i in range(len(arr)+1)]

for i in range(1, len(arr)+1):
    arr_pref[i] = arr_pref[i-1] + arr[i-1]

answer = arr_pref[1]
for i in range(1, len(arr)+1):
    for j in range(0, i):
        if sum(arr[:j])>answer:
            answer = sum(arr[:j])
print(answer)


# 5
# -7 5 4 -10 4
