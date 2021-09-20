s = input().split()
arr = []
for i in range(len(s)):
    if s[i] == '2':
        arr.append(i)

max_all = -1
for i in range(len(s)):
    if s[i] == '1':
        min_num = 10
        for j in arr:
            if abs(i - j) < min_num:
                min_num = abs(i - j)
        if min_num > max_all:
            max_all = min_num
print(max_all)
