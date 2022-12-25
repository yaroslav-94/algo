# Простое решение не проходит по времени
def count_inversions(arr: list):
    ans = 0
    for i in range(len(arr) - 1):
        value = 0
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                value += 1
        ans += value
    return ans


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    answer = count_inversions(arr)
    print(answer)


if __name__ == "__main__":
    main()
