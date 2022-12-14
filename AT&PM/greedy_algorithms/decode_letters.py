def decode_string(s: str):
    d_ans = {}
    for i in s:
        if i not in d_ans.keys():
            d_ans[i] = 1
        else:
            d_ans[i] += 1

    arr_ans = [(key, val) for key, val in d_ans.items()]
    arr_ans.sort(key=lambda x: x[1])

    arr_dec = []
    while len(arr_ans) > 1:
        arr_dec.append((arr_ans[0][0], 0))
        arr_dec.append((arr_ans[1][0], 1))
        arr_ans.append((arr_ans[0][0] + arr_ans[1][0], arr_ans[0][1] + arr_ans[1][1]))
        del arr_ans[0]
        del arr_ans[0]
        arr_ans.sort(key=lambda x: x[1])

    if not arr_dec:
        arr_dec.append((arr_ans[0][0], 0))

    fin_answer = {}
    for let in d_ans.keys():
        let_code = ''
        for pair in arr_dec:
            if pair[0].count(let) > 0:
                let_code += str(pair[1])
        fin_answer[let] = let_code[::-1]

    return fin_answer


def main():
    s_inp = input()
    d_let = decode_string(s_inp)

    # decode string
    s_dec = []
    for i in s_inp:
        s_dec.append(d_let[i])
    s_dec = ''.join(str(i) for i in s_dec)
    print(len(d_let), len(s_dec))

    # print letters and text
    for key, val in d_let.items():
        print(f"{key}:{val}")
    print(s_dec)


if __name__ == "__main__":
    main()
