a, k, b, m, x = map(int, input().split())
l = 0
r = x * (max(a,b) + max(a,b)%2)


def count_trees(days):
    destr_first = a * days - int(days // k) * a
    destr_second = b * days - int(days // m) * b
    return destr_first + destr_second

while l<r:
    days = (l+r)//2
    if count_trees(days)<x:
        l = days+1
    else:
        r = days
print(l)
#
