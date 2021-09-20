all_num, start, end = list(map(lambda x: int(x), input().split()))
answer = min(abs(end-start)-1, all_num-abs(start-end)-1)
print(answer)
