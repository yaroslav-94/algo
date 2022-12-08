def fib_mod(n, m):
    if n == 1:
        return 1
    elif n >= 1:
        left, right = 1, 1
        arr = [0, 1, 1]
        for i in range(2, n):
            left, right = right % m, (left + right) % m
            if right not in arr:
                arr.append(right)
            else:
                break
        return arr[n%len(arr)]

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
