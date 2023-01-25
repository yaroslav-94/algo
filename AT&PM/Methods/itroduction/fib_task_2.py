def fib_digit(n):
    if n == 1:
        return 1
    elif n >= 1:
        left, right = 1, 1
        for i in range(2, n):
            left, right = right % 10, (left + right) % 10
        return right


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
