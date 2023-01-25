import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    # создаем кучу из частот и символов в строке
    h = []
    # гарантируется уникальное значение, которое можно сравнивать
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def test(n_iter=100) -> None:
    """
    Нужно добавить декодирование строки
    :param n_iter:
    :return: None
    """
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        # assert huffman_decode(encoded, code) == s


def main():
    s = input()
    code = huffman_encode(s)
    print(code)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()
