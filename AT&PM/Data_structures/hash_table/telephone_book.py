def main():
    n = int(input())

    d = {}
    for _ in range(n):
        arr = input().split()
        if arr[0].startswith('add'):
            d[arr[1]] = arr[2]
        elif arr[0].startswith('del'):
            if arr[1] in d:
                del d[arr[1]]
        elif arr[0].startswith('find'):
            if arr[1] in d:
                print(d[arr[1]])
            else:
                print('not found')


if __name__ == "__main__":
    main()
