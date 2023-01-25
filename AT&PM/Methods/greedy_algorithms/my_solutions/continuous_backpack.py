def find_max_coast(arr: list, w: int):
    if w == 0:
        return 0
    else:
        answer = 0
        ind = 0
        while w > 0 and ind < len(arr):
            if w >= arr[ind][1]:
                w -= arr[ind][1]
                answer += arr[ind][0]
                ind += 1
            else:
                part = arr[ind][1] / w
                w = 0
                answer += part * arr[ind][0]
        return round(answer, 3)


def main():
    n, w = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: x[0] / x[1], reverse=True)
    answer = find_max_coast(arr, w)
    print(answer)


if __name__ == "__main__":
    main()
