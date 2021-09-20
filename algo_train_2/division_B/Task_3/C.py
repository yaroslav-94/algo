arr = list(map(int, input().split()))
d = {}
answer = []

for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for key, value in d.items():
    if value == 1:
        answer.append(str(key))
print(' '.join(answer))
