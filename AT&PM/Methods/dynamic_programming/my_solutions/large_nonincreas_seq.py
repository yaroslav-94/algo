import sys


def lis_bottom_down(arr: list):
    d = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        d[i] = 1
        for j in range(i):
            if arr[j] >= arr[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    if len(arr) > 1:
        max_v, max_ind = d[0], 0
        for i in range(len(d)):
            if d[i] >= max_v:
                max_v = d[i]
                max_ind = i
        arr_answer = [0 for _ in range(max_v)]

        while max_v > 0:
            arr_answer[max_v - 1] = max_ind + 1
            j = max_ind - 1
            while j > 0:
                if d[j] == max_v - 1 and arr[j] >= arr[max_ind]:
                    break
                j -= 1
            max_ind = j
            max_v -= 1
        return arr_answer
    else:
        return arr


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    next(reader)
    arr = next(reader)
    answer = lis_bottom_down(arr)
    print(len(answer))
    print(' '.join(str(i) for i in answer))


if __name__ == "__main__":
    main()