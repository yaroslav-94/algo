class JoinSet:
    def __init__(self, size: int = None, arr: list = None):
        self.parent = [0 for _ in range(size + 1)]
        self.rank = [0 for _ in range(size + 1)]
        self.values = arr if arr else []
        self.max_val = max(self.values)

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            print(self.max_val)
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
        self.values[j_id - 1] += self.values[i_id - 1]
        self.values[i_id - 1] = self.values[j_id - 1]
        if self.values[i_id - 1] > self.max_val:
            self.max_val = self.values[i_id - 1]
        print(self.max_val)


def main():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    js = JoinSet(size=n, arr=arr)
    for _ in range(m):
        des, sou = list(map(int, input().split()))
        js.union(des, sou)


if __name__ == "__main__":
    main()
