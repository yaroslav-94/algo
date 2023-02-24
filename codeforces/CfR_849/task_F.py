import sys

reader = (map(int, line.split()) for line in sys.stdin)

t = next(reader)


def sum_numbers(num: int):
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num = num // 10
    return sum_num


for i in range(t):
    n, q = next(reader)
    arr = next(reader)
    for j in range(q):
        act = next(reader)
        if act[0] == 1:
            for k in range(act[1] - 1, act[2]):
                arr[k] = sum_numbers(arr[k])
        elif act[0] == 2:
            print(arr[act[1] - 1])
