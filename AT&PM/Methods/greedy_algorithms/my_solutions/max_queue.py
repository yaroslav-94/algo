class QueueMax:
    def __init__(self):
        self.data = []
        self.size = len(self.data)

    def __prepare_queue_up(self, ind: int):
        while (self.data[ind] > self.data[(ind - 1) // 2]) and (ind > 0):
            self.data[ind], self.data[(ind - 1) // 2] = self.data[(ind - 1) // 2], self.data[ind]
            ind = (ind - 1) // 2

    def __prepare_queue_down(self, ind: int):
        while 2 * ind + 1 < self.size:
            left = 2 * ind + 1
            right = 2 * ind + 2
            j = left
            if right < self.size and self.data[right] > self.data[left]:
                j = right
            if self.data[ind] > self.data[j]:
                break
            self.data[ind], self.data[j] = self.data[j], self.data[ind]
            ind = j

    def extract_max(self):
        print(self.data[0])
        self.data[0] = self.data[-1]
        del self.data[-1]
        self.size = len(self.data)
        self.__prepare_queue_down(ind=0)

    def insert(self, num: int):
        self.data.append(num)
        self.size = len(self.data)
        self.__prepare_queue_up(ind=self.size - 1)


def main():
    import sys

    q = QueueMax()
    n = int(sys.stdin.readline())
    for i in range(n):
        s = sys.stdin.readline()
        if s.startswith('Insert'):
            q.insert(int(s.split(' ')[1]))
        elif s.startswith('ExtractMax'):
            q.extract_max()


if __name__ == "__main__":
    main()
