def lestniza_recursion(n: int, arr: list):
    """
    Find max sum. Time limit
    :param n: number of steps
    :param arr: array with coasts steps
    :return: max sum
    """
    d = [0 for _ in range(n + 1)]

    def recursion(t: int):
        if t == 0:
            return 0
        if t == 1:
            d[1] = arr[0]
            return d[1]
        pred1 = recursion(t - 1)
        pred2 = recursion(t - 2)
        d[t] = max(pred1 + arr[t - 1], pred2 + arr[t - 1])
        return d[t]

    recursion(n)
    return d[n]


def lestniza_with_array(n: int, arr: list):
    d = [0 for _ in range(n + 1)]

    for i in range(1, len(arr)):
        d[i] = max(d[i - 1] + arr[i - 1], d[i - 2] + arr[i - 1])

    return d[n]


def lestniza(arr: list):
    start, end = 0, 0

    for i in range(len(arr)):
        start, end = end, max(start + arr[i], end + arr[i])
    return end


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    answer = lestniza(arr)
    print(answer)


if __name__ == "__main__":
    main()
