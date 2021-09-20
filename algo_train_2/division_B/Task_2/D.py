len_val, num_point = list(map(lambda x: int(x), input().split()))
coord = list(map(lambda x: int(x), input().split()))

if len_val % 2 == 1 and coord.count(len_val // 2) == 1:
    print(len_val // 2)
else:
    l_num = 0
    r_num = 0
    for i in range(1, len_val // 2):
        if coord.count(len_val // 2 - i) == 1:
            l_num = len_val // 2 - i
            break

    for i in range(len_val // 2):
        if coord.count(len_val // 2 + i) == 1:
            r_num = len_val // 2 + i
            break

    print(l_num, r_num)
