def lis_bottom_up(arr: list):
    d = [0 for _ in range(len(arr))]
    for i in range(len(arr)):
        d[i] = 1
        for j in range(i):
            if arr[i] % arr[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    answer = 0
    for i in d:
        if i > answer:
            answer = i
    return answer


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    answer = lis_bottom_up(arr)
    print(answer)


if __name__ == "__main__":
    main()
