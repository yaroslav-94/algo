max_num = int(input())
s = ''
s_num = ''
s_ans = ''
ind_s = 0
d = {
    'YES': set(),
    'NO': set()
}
while s != "HELP":

    if s_num == '' and ind_s % 2 == 1:
        s_num = s

    elif s_ans == '' and ind_s % 2 == 0:
        s_ans = s

    if s_ans == 'YES' and s_num != '':
        if d['YES'] == set():
            d['YES'].update(set(map(int, s_num.split())))
        else:
            d['YES'].intersection_update(set(map(int, s_num.split())))
        s_ans = ''
        s_num = ''
    elif s_ans == "NO" and s_num != '':
        d['NO'].update(set(map(int, s_num.split())))
        s_ans = ''
        s_num = ''

    s = input()
    ind_s += 1

if d['YES'] == set():
    d['YES'].update(set(range(1, max_num + 1)))

print(' '.join(str(i) for i in sorted(d['YES'] - d['NO'])))
