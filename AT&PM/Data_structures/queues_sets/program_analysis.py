class JoinSet:
    def __init__(self, size: int = None):
        self.parent = [i for i in range(size + 1)]
        self.rank = [0 for _ in range(size + 1)]

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

    def equal(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return True
        return False


def main():
    n, e, d = list(map(int, input().split()))
    js = JoinSet(size=n)
    for _ in range(e):
        des, sou = list(map(int, input().split()))
        js.union(des, sou)

    answer = 1
    for _ in range(d):
        des, sou = list(map(int, input().split()))
        if not js.equal(des, sou):
            answer = 0
            break
    print(answer)


if __name__ == "__main__":
    main()
