def main():
    d_let = {}
    k, _ = map(int, input().split())
    for i in range(k):
        key, val = input().split(': ')
        d_let[key] = val
    text_for_encode = input()

    d_dec_let = {
        val: key for key, val in d_let.items()
    }

    ind_right = 1
    ind_left = 0
    answer = []
    while ind_right <= len(text_for_encode):
        while text_for_encode[ind_left:ind_right] not in d_dec_let:
            ind_right += 1
        answer.append(d_dec_let[text_for_encode[ind_left:ind_right]])
        ind_left, ind_right = ind_right, ind_right + 1
    print(''.join(i for i in answer))
    # return ''.join(i for i in answer)


if __name__ == "__main__":
    main()
