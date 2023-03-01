class MinQueue:

    def __init__(self, arr: list):
        self.data = arr
        self.size = len(self.data)

    def sift_down(self, ind: int):
        pairs = []
        while 2 * ind + 1 < self.size:
            left = 2 * ind + 1
            right = 2 * ind + 2
            j = left
            if right < self.size and self.data[right] < self.data[left]:
                j = right
            if self.data[ind] < self.data[j]:
                break
            self.data[ind], self.data[j] = self.data[j], self.data[ind]
            pairs.append(f'{ind} {j}')
            ind = j
        return pairs

    def heapify(self):
        ans = []
        for i in range(self.size // 2, -1, -1):
            ans += self.sift_down(ind=i)
        return ans


if __name__ == "__main__":
    _ = int(input())
    arr = list(map(int, input().split()))
    mq = MinQueue(arr)
    answer = mq.heapify()

    print(len(answer))
    for s in answer:
        print(s)
