d = int(input())
x, y = list(map(lambda x: int(x), input().split()))

if ((0 <= x <= d and 0 <= y <= d and y <= -x + d and d > 0 and x >= 0 and y >= 0) or
        (0 >= x >= d and 0 >= y >= d and y >= -x + d) and d < 0 and x <= 0 and y <= 0):
    print(0)
else:
    d_A = (x ** 2 + y ** 2) ** (1 / 2)
    d_B = ((x - d) ** 2 + y ** 2) ** (1 / 2)
    d_C = (x ** 2 + (y - d) ** 2) ** (1 / 2)
    if d_A == min(d_A, d_B, d_C):
        print(1)
    elif d_B == min(d_A, d_B, d_C):
        print(2)
    else:
        print(3)
