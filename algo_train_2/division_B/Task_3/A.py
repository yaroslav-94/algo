arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

print(len(set(arr_1) & set(arr_2)))
