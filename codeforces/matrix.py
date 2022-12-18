answer = []
t = int(input())
for i in range(t):
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    matrix = [line1, line2]
    fl = False
    for i in range(4):
        matrix = [[matrix[1][0], matrix[0][0]], [matrix[1][1], matrix[0][1]]]
        if (matrix[0][0] < matrix[0][1]) and (matrix[1][0] < matrix[1][1]) and (matrix[0][0] < matrix[1][0]) and (
                matrix[0][1] < matrix[1][1]):
            fl = True
            break

    if fl:
        answer.append('YES')
    else:
        answer.append('NO')

for i in range(t):
    print(answer[i])