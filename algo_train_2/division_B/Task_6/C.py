param = list(map(int, input().split()))


def count_value(param, value):
    return param[0] * value ** 3 + param[1] * value ** 2 + param[2] * value + param[3]


def find_value(param, l, r, eps):
    if param[0]>0:
        while l + eps < r:
            m = (l + r) / 2
            if count_value(param, m) <= 0:
                l = m
            else:
                r = m
    else:
        while l + eps < r:
            m = (l + r) / 2
            if count_value(param, m) <= 0:
                r = m
            else:
                l = m
    return l


eps = 0.000_01
m = 10_000_000
answer = find_value(param, l=-m, r=m, eps=eps)
print(answer)

