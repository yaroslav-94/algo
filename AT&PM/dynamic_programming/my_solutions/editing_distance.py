def edit_dist_bu(s1: str, s2: str):
    n = len(s1)
    m = len(s2)
    d = [
        [0 for _ in range(m + 1)] for _ in range(n + 1)
    ]

    for i in range(n + 1):
        d[i][0] = i

    for i in range(m + 1):
        d[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 0 if s1[i - 1] == s2[j - 1] else 1

            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + c
            )

    return d[n][m]


def main():
    s1 = input()
    s2 = input()
    answer = edit_dist_bu(s1, s2)
    print(answer)


if __name__ == "__main__":
    main()
