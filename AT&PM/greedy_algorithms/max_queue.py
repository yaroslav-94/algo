class QueueMax:

    def __init__(self):
        self.data = []

    def __prepare_queue(self):
        i = len(self.data) - 1
        while i > 0:
            up_val = i // 2
            j = up_val
            if 0 < up_val < len(self.data) and self.data[up_val] > self.data[i]:
                j = up_val
            if self.data[i] <= self.data[j]:
                break
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i = j

    def insert(self, num: int):
        self.data.append(num)
        self.__prepare_queue()

    def extract_max(self):
        print(self.data[0])
        del self.data[0]
        self.__prepare_queue()


def main():
    q = QueueMax()
    n = int(input())
    for i in range(n):
        s = input()
        if s.startswith('Insert'):
            q.insert(int(s.split(' ')))
        elif s.startswith('ExtractMax'):
            q.extract_max()


if __name__ == "__main__":
    main()
