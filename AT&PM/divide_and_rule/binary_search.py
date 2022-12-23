def binary_search(arr_sort: list, arr_find: list):
    answer = []
    for i in arr_find:
        left = 0
        right = len(arr_sort)
        fl = 0
        while left < right:
            middle = (left + right) // 2
            if arr_sort[middle] > i:
                right = middle
            elif arr_sort[middle] < i:
                left = middle + 1
            else:
                fl = 1
                answer.append(middle + 1)
                break
        if not fl:
            answer.append(-1)
    return answer


def main():
    _, *arr_sort = list(map(int, input().split()))
    _, *arr_find = list(map(int, input().split()))
    answer = binary_search(arr_sort, arr_find)
    print(' '.join(str(i) for i in answer))


if __name__ == "__main__":
    main()
