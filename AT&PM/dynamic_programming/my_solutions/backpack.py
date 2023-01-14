def knapsack_without_reps_bu(back: int, weights: list):
    costs = weights
    d = [[0 for _ in range(back + 1)] for _ in range(len(costs))]

    for i in range(len(costs)):
        for w in range(1, back + 1):
            # заполняем теущий рюкзак предметами как предыдущий - не учитываем новый предмет
            d[i][w] = d[i - 1][w]
            # если текущий элемент вмещается в рюкзак, то проверяем - стало ли лучше при его добавлении
            if weights[i] <= w:
                d[i][w] = max(
                    d[i][w], d[i - 1][w - weights[i]] + costs[i]
                )

    return d[len(costs) - 1][back]


def main():
    back, _ = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    answer = knapsack_without_reps_bu(back, weights)
    print(answer)


if __name__ == "__main__":
    main()
