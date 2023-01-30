from queue import LifoQueue


def is_balaned(s: str):
    q = LifoQueue()
    ind = LifoQueue()
    for i in range(len(s)):
        if s[i] in {'(', '[', '{'}:
            q.put(s[i])
            ind.put(i + 1)
        elif s[i] in {')', ']', '}'}:
            if q.qsize() == 0:
                return i + 1
            top = q.get()
            ind.get()
            if top == '(' and s[i] != ')' or top == '[' and s[i] != ']' or top == '{' and s[i] != '}':
                return i + 1
    if q.qsize() > 0:
        return ind.get()
    return 'Success'


def main():
    s = input()
    answer = is_balaned(s)
    print(answer)


if __name__ == "__main__":
    main()
