from collections import deque


def find_max_window(n: int, arr: list, m: int):
    answer = []
    input_val = deque()
    output_val = deque()
    max_val = 0

    for i in range(len(arr)):
        if len(input_val) < m and len(output_val) == 0:
            if arr[i] > max_val:
                max_val = arr[i]
            input_val.append((arr[i], max_val))

        elif len(input_val) == m:
            max_val = 0
            for _ in range(m):
                val = input_val.pop()
                if max_val < val[0]:
                    max_val = val[0]
                output_val.append((val[0], max_val))
            answer.append(output_val.pop()[1])
            max_val = arr[i]
            input_val.append((arr[i], max_val))

        else:
            max_now = max(max_val, output_val.pop()[1])
            answer.append(max_now)
            if arr[i] > max_val:
                max_val = arr[i]
            input_val.append((arr[i], max_val))

    while min(len(output_val), len(input_val)) > 0:
        max_now = max(input_val.pop()[1], output_val.pop()[1])
        answer.append(max_now)

    while len(input_val) >= m:
        answer.append(input_val.pop()[1])

    return answer


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
answer = find_max_window(n, arr, m)
print(*answer)
