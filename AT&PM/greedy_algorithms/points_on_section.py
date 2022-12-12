def find_points(arr: list):
    i = 1
    ind_ans = 0
    answer = [arr[0][1]]
    while i < len(arr):
        if arr[i][0] <= answer[ind_ans] <= arr[i][1]:
            i += 1
        else:
            answer.append(arr[i][1])
            ind_ans += 1
            i += 1
    return answer


def main():
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: x[1])
    answer = find_points(arr)
    print(len(answer))
    print(' '.join(str(i) for i in answer))


if __name__ == "__main__":
    main()
