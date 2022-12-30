import sys


def partition(arr: list, l_index: int, r_index: int):
    sup_el = arr[(l_index+r_index)//2]
    i = l_index
    gt = r_index
    lt = l_index
    while i <= gt:
        if arr[i] < sup_el:
            arr[i], arr[lt] = arr[lt], arr[i]
            i += 1
            lt += 1
        elif arr[i] > sup_el:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def quick_sort(arr: list, l: int = 0, r: int = None):
    if r is None:
        r = len(arr)-1
    if l >= r:
        return
    left, right = partition(arr, l, r)
    quick_sort(arr, l, left - 1)
    quick_sort(arr, right + 1, r)


def find_min(arr: list, value: int):
    """
    Find index in array where value>=arr[left_ind]
    """
    left_ind = 0
    right_ind = len(arr)
    while left_ind<right_ind:
        middle = (left_ind+right_ind)//2
        if arr[middle]>value:
            right_ind = middle
        elif arr[middle]<=value:
            left_ind = middle+1
    return left_ind


def find_max(arr: list, value: int):
    """
    Find index in array where value<=arr[left_ind]
    """
    left_ind = 0
    right_ind = len(arr)
    while left_ind<right_ind:
        middle = (left_ind+right_ind)//2
        if arr[middle]>=value:
            right_ind = middle
        elif arr[middle]<value:
            left_ind = middle+1
    return left_ind


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, m = next(reader)
    start_sec = []
    end_sec = []
    for _ in range(n):
        sec = next(reader)
        start_sec.append(sec[0])
        end_sec.append(sec[1])
    points = next(reader)

    # sorting start points
    quick_sort(start_sec)
    quick_sort(end_sec)

    answer = []
    for i in range(m):
        # find first element in start_sec>=points[i]
        ind_start = find_min(start_sec, points[i])

        # find last element in end_sec<=points[i]
        ind_end = find_max(end_sec, points[i])

        # count number sections
        answer.append(ind_start - ind_end)

    print(' '.join(str(i) for i in answer))


if __name__ == "__main__":
    main()
