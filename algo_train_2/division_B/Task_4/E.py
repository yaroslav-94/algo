sum_msg = int(input())
all_names = {}
counter_msg = 0
max_sum_msg_name = [0, '']

while sum_msg != counter_msg:
    counter_msg += 1
    num_msg = int(input())

    if num_msg == 0:
        name = input()
        msg = input()
        all_names[name] = [counter_msg]
        if max_sum_msg_name[0] == 0:
            max_sum_msg_name = [1, name]

    elif num_msg > 0:
        msg = input()
        for key in all_names.keys():
            if all_names[key].count(num_msg) > 0:
                all_names[key].append(counter_msg)
                if len(all_names[key]) > max_sum_msg_name[0]:
                    max_sum_msg_name = [len(all_names[key]), key]

print(max_sum_msg_name[1])
