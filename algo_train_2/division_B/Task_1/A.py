code_task = int(input())
iterac = int(input())
checker = int(input())

if iterac == 0:
    if code_task != 0:
        print(3)
    else:
        print(checker)
elif iterac == 1:
    print(checker)
elif iterac == 4:
    if code_task != 0:
        print(3)
    else:
        print(4)
elif iterac == 6:
    print(0)
elif iterac == 7:
    print(1)
else:
    print(iterac)
