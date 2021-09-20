m = int(input())

num_see = []
for i in range(m):
    num_see.append(input())

n = int(input())


def number_agree(auto_num, arr_see):
    sum_numbers = 0
    for i in arr_see:
        see = True
        for j in set(i):
            if auto_num.count(j) == 0:
                see = False
        sum_numbers += int(see)
    return sum_numbers


max_see = 0
answer = []
for i in range(n):
    new_auto = input()
    num_new_auto = number_agree(auto_num=new_auto, arr_see=num_see)
    if max_see < num_new_auto:
        max_see = num_new_auto
        answer = []

    if max_see == num_new_auto:
        answer.append(new_auto)

print('\n'.join(i for i in answer))
