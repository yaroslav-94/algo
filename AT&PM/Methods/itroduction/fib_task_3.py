def fib_mod(n, m):
    if n == 1:
        return 1
    elif n >= 1:
        left, right = 1, 1
        arr = [0, 1, 1]
        indexes = [0]

        # записываем все разности для поиска периода
        for i in range(3, 6 * m):
            left, right = right % m, (left + right) % m
            arr.append(right)
            if right == 1 and left == 0:
                indexes.append(i - 1)

        # проверка на период
        find_p = set()
        for j in range(len(indexes) - 1):
            find_p.add(indexes[j + 1] - indexes[j])
        return arr[n % (find_p.pop())]

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

# 10 2 1
# 1025 55 - 5
# 12589 369 - 89
# 1598753 25897 - 20305
# "n": "60282445765134413", "m": 2263, "expected": 974
