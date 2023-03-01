import heapq


def main():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    cpus = [(0, i) for i in range(n)]

    for i in range(m):
        if len(cpus) < n:
            heapq.heappush(cpus, (arr[i], i))
            print(f'{i} {0}')
        else:
            a = heapq.heappop(cpus)
            print(f'{a[1]} {a[0]}')
            heapq.heappush(cpus, (a[0] + arr[i], a[1]))


if __name__ == "__main__":
    main()
