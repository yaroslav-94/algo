import sys
from collections import deque


class Stec:

    def __init__(self):
        self.val_max = deque()

    def push(self, elem: int):
        if len(self.val_max) == 0:
            self.val_max.append(elem)
        else:
            self.val_max.append(max(self.val_max[-1], elem))

    def max_val(self):
        return self.val_max[-1]

    def pop_el(self):
        self.val_max.pop()


arr = Stec()
reader = (line for line in sys.stdin)
q = int(next(reader))
for _ in range(q):
    s = next(reader)
    if s.startswith('push'):
        arr.push(int(s.split()[1]))
    if s.startswith('max'):
        print(arr.max_val())
    if s.startswith('pop'):
        arr.pop_el()
