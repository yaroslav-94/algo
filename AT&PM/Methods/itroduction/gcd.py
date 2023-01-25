def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    elif a == 1 or b == 1:
        return 1
    else:
        if a > b:
            a = a % b
        else:
            b = b % a
        return gcd(a, b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
