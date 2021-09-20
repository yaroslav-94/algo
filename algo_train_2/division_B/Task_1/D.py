num = int(input())
arr = list(map(lambda x: int(x), input().split()))
index = int((len(arr) - 1) // 2)
print(arr[index])
