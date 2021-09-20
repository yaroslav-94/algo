with open('input.txt') as f:
    s = f.readline()
    d_final = {}
    while s:
        name, value = s.split()
        if name in d_final:
            d_final[name] += int(value)
        else:
            d_final[name] = int(value)
        s = f.readline()

for key in sorted(d_final.keys()):
    print(key, d_final[key])
