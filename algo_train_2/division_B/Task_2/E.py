num = int(input())
s = list(map(int, input().split()))
if num == 1:
    print(0)
else:
    print(sum(s)-max(s))
