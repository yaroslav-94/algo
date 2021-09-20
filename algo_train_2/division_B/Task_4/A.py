n = int(input())
d = {}

for i in range(n):
    color, value = list(map(int, input().split()))
    if color in d:
        d[color] += value
    else:
        d[color] = value

for key in sorted(d.keys()):
    print(key, d[key])
