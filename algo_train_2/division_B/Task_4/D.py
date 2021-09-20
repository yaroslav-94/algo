with open('input.txt') as f:
    s = f.readline()
    d_data = {}
    all_sum = 0
    while s:
        name = s[:s.rindex(' ')]
        number = int(s[s.rindex(' ')::])
        if name in d_data:
            d_data[name] += number
        else:
            d_data[name] = number
        all_sum += number
        s = f.readline()

d_answer = {}
frst_sum = 0
arr_balance = []
for key, value in d_data.items():
    l = int(value / all_sum * 450)
    d_answer[key] = l
    arr_balance.append((value / all_sum * 450 - l, value, key))
    frst_sum += l
arr_balance.sort(reverse=True)

if frst_sum < 450:
    i = 0
    while frst_sum < 450:
        d_answer[arr_balance[i][2]] += 1
        frst_sum += 1
        i += 1

for key, value in d_answer.items():
    print(key, value)
