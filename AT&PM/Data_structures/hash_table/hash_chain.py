def hash_func(m: int, s: str):
    p = 1_000_000_007
    x = 263
    sum_val = 0
    for i in range(len(s)):
        sum_val += (ord(s[i])*x**i)%p
    return sum_val%p%m

def main():
    m = int(input())
    n = int(input())
    table = [[] for _ in range(m)]

    for _ in range(n):
        arr = input().split()
        if arr[0].startswith('add'):
            h = hash_func(m=m, s=arr[1])
            if arr[1] not in table[h]:
                table[h] = [arr[1]] + table[h]

        elif arr[0].startswith('del'):
            h = hash_func(m=m, s=arr[1])
            if arr[1] in table[h]:
                table[h].pop(table[h].index(arr[1]))

        elif arr[0].startswith('find'):
            h = hash_func(m=m, s=arr[1])
            if table[h] is None or arr[1] not in table[h]:
                print('no')
            else:
                print('yes')

        elif arr[0].startswith('check'):
            print(' '.join(table[int(arr[1])]))


if __name__ == "__main__":
    main()