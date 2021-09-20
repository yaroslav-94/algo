arr = list(map(int, input().split()))
s = set()
for i in arr:
    if i in s:
        print("YES")
    else:
        s.add(i)
        print("NO")
