def calk(n: int):
    d = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        val1, val2, val3 = i - 1, i - 1, i - 1
        if i % 2 == 0:
            val1 = i // 2
        if i % 3 == 0:
            val2 = i // 3
        d[i] = min(
            d[val1] + 1,
            d[val2] + 1,
            d[val3] + 1
        )

    ind = n
    ret_arr = [n]
    while ind > 1:
        if d[ind - 1] + 1 == d[ind]:
            ret_arr.append(ind - 1)
            ind -= 1
        elif ind % 2 == 0 and d[ind // 2] + 1 == d[ind]:
            ret_arr.append(ind // 2)
            ind = ind // 2
        else:
            ret_arr.append(ind // 3)
            ind = ind // 3

    return d[n], ret_arr[::-1]


def main():
    n = int(input())
    answer, arr = calk(n)
    print(answer)
    print(' '.join(str(i) for i in arr))


if __name__ == "__main__":
    main()
