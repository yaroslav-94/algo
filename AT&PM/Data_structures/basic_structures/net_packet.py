from collections import deque


def proc_work():
    size, n = list(map(int, input().split()))
    answer = []
    q = deque()

    for i in range(n):
        arrival, durat = list(map(int, input().split()))
        if len(q) == 0:
            q.append((arrival, durat, i))
        elif len(q) < size:
            q.append((max(arrival, q[-1][0] + q[-1][1]), durat, i))
        elif arrival >= (q[0][1] + q[0][0]):
            first = q.popleft()
            answer.append((first[2], first[0]))
            if len(q) == 0:
                q.append((arrival, durat, i))
            else:
                q.append((max(arrival, q[-1][0] + q[-1][1]), durat, i))
        else:
            answer.append((i, -1))

    while len(q) > 0:
        first = q.popleft()
        answer.append((first[2], first[0]))
    answer.sort()
    answer = [a[1] for a in answer]
    for i in answer:
        print(i)


if __name__ == "__main__":
    proc_work()
