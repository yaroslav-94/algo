def fib(n):
    if n == 1:
        return 1
    elif n >= 1:
        left, right = 1, 1
        for i in range(2, n):
            left, right = right, left + right
        return right


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
