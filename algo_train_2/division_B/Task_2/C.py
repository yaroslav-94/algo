s = input()
if len(s) == 1:
    print(0)
else:
    sum_mon = 0
    for i in range(len(s) // 2 + len(s) % 2):
        if s[i] != s[len(s) - i - 1]:
            sum_mon += 1
    print(sum_mon)
