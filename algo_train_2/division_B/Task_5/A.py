n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr_pref = [0 for i in range(len(arr)+1)]

for i in range(1, len(arr)+1):
    arr_pref[i] = arr_pref[i-1] + arr[i-1]

answer = []
for i in range(q):
    l, r = map(int, input().split())
    answer.append(arr_pref[r] - arr_pref[l-1])

# Best speed, good memory
print('\n'.join(str(i) for i in answer)+'\n')

# Good speed, best memory
print(* answer)
