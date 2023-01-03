def count_sort(arr: list):
    M = max(arr) + 1
    d_uniq = [0 for i in range(M)]
    new_arr = [0 for i in range(len(arr))]

    for j in arr:
        d_uniq[j] += 1

    for i in range(1, M):
        d_uniq[i] += d_uniq[i - 1]

    j = len(arr) - 1
    while j >= 0:
        new_arr[d_uniq[arr[j]] - 1] = arr[j]
        d_uniq[arr[j]] -= 1
        j -= 1
    return new_arr


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    new_arr = count_sort(arr)
    print(' '.join(str(i) for i in new_arr))


if __name__ == "__main__":
    main()
