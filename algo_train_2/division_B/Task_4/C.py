with open('input.txt') as f:
    s = f.readline()
    d_final = {}
    while s:
        for i in s.split():
            if i in d_final:
                d_final[i] += 1
            else:
                d_final[i] = 1
        s = f.readline()

b = list([(value, key) for key, value in d_final.items()])
b.sort()
for i in sorted(b, key=lambda x: x[0], reverse=True):
    print(i[1])
