max_now = num_now = int(input())
sum_max = 0
while num_now != 0:
    if num_now > max_now:
        max_now = num_now
        sum_max = 0
    if num_now == max_now:
        sum_max += 1
    num_now = int(input())
print(sum_max)
