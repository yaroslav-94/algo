import sys
sys.setrecursionlimit(3000000)


def find_height(arr: list):
    d_trie = {}
    r = 0

    for i in range(len(arr)):
        if arr[i] == -1:
            r = i
        elif arr[i] not in d_trie:
            d_trie[arr[i]] = [i]
        else:
            d_trie[arr[i]].append(i)

    def height(root: int):
        h = 1
        if root in d_trie:
            for child in d_trie[root]:
                h = max(h, 1 + height(child))
        return h
    answer = height(r)
    return answer


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    answer = find_height(arr)
    print(answer)


if __name__ == "__main__":
    main()
