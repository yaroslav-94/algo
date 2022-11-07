a, k, b, m, x = map(int, input().split())

day_work_num = 1
while x>0:
    if day_work_num % k != 0:
        x -= a
    if day_work_num % m != 0:
        x-= b
    day_work_num += 1

print(day_work_num-1)
# a = 2
# k = 2
# b = 3
# m = 2
# def count_trees(days):
#     destr_first = a * days - int(days // k) * a
#     destr_second = b * days - int(days // m) * b
#     return destr_first + destr_second
# print(count_trees(400000000000000000))
# print(1000000000000000000 == 1000000000000000000)