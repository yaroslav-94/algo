# # Простое решение не проходит по времени
# def count_inversions(arr: list):
#     ans = 0
#     for i in range(len(arr) - 1):
#         value = 0
#         for j in range(i, len(arr)):
#             if arr[i] > arr[j]:
#                 value += 1
#         ans += value
#     return ans
#
#

def merge(arr1: list, arr2: list, counter: int) -> tuple:
    i, j = 0, 0
    answer = []
    counter += arr1[1] + arr2[1]
    arr1 = arr1[0]
    arr2 = arr2[0]

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            answer.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            answer.append(arr2[j])
            counter += len(arr1) - i
            j += 1

    if i == len(arr1) and j < len(arr2):
        answer += arr2[j:]
    elif i < len(arr1) and j == len(arr2):
        answer += arr1[i:]
    return answer, counter


def count_inversions(arr: list, counter: int = 0) -> tuple:
    if len(arr) == 1:
        return arr, counter
    else:
        m = len(arr) // 2
        return merge(count_inversions(arr[:m], counter), count_inversions(arr[m:], counter), counter)


def main() -> None:
    _ = int(input())
    arr = list(map(int, input().split()))
    answer = count_inversions(arr)
    print(answer)


if __name__ == "__main__":
    main()


# answer = count_inversions(arr=[7, 6, 5, 4, 3, 2, 1])
# assert answer[1] == 21, "1 Answer {}".format(answer)
#
# answer = count_inversions(arr=[3, 2, 1])
# assert answer[1] == 3, "2 Answer {}".format(answer)
#
# answer = count_inversions(arr=[2, 3, 9, 2, 9])
# assert answer[1] == 2, "3 Answer {}".format(answer)