def find_all_terms(n: int):
    if n == 1:
        return [1]
    else:
        answer = []
        for i in range(1, n+1):
            if (n - i) >= i + 1 or (n - i) == 0:
                answer.append(i)
                n -= i
            if n == 0:
                break
        return answer


def main():
    n = int(input())
    answer = find_all_terms(n)
    print(len(answer))
    print(' '.join(str(i) for i in answer))


if __name__ == "__main__":
    main()
