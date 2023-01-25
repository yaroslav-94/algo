import sys
import heapq


def fractional_knapsack(capacity: int, values_and_weights: list):
    # - для того, чтобы все было нормально в мин-куче
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)

    acc = 0
    while order and capacity:
        # берем корень из кучи
        v_per_w, w = heapq.heappop(order)
        # ищем минимум
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take

    return acc


def main():
    # читаем из стандартного потого ввода быстрее
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(opt_value))


def test():
    assert fractional_knapsack(0, [(60, 20)]) == 0.0
    assert fractional_knapsack(25, [(60, 20)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (0, 100)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 65
    assert fractional_knapsack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0

    from random import randint
    from time import time
    for attempt in range(100):
        n = randint(1, 1000)
        capacity = randint(0, 2 * 10 ** 6)
        values_and_weights = []
        for i in range(n):
            values_and_weights.append(
                (randint(0, 2 * 10 ** 6), randint(1, 2 * 10 ** 6))
            )
        t = time()
        _ = fractional_knapsack(capacity, values_and_weights)
        assert time() - t < 5


if __name__ == "__main__":
    main()
