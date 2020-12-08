

def gen_group_anws():
    '''
        dictionary generator
    '''

    with open('day_6/input.txt') as in_txt:

        cur_line = in_txt.readline().replace('\n', '')

        cur_group_answs = {}
        cur_group_answs['num_grp_mbrs'] = 0
        while cur_line:

            # new line character has lenght of 1
            if len(cur_line) < 2:

                yield cur_group_answs
                cur_group_answs = {}
                cur_group_answs['num_grp_mbrs'] = 0

            else:
                cur_line = cur_line.replace('\n', '')

                for ques_val in cur_line:
                    if ques_val in cur_group_answs:
                        cur_group_answs[ques_val] += 1
                    else:
                        cur_group_answs[ques_val] = 1
                cur_group_answs['num_grp_mbrs'] += 1

            cur_line = in_txt.readline()

        yield cur_group_answs


group_anws_generator = gen_group_anws()

total_group_sum = 0
all_yes_sum = 0
for group_anws in group_anws_generator:

    # part 1 processing
    num_ans = len(list(group_anws))
    total_group_sum += num_ans

    # part 2 processing
    num_mbrs = group_anws['num_grp_mbrs']
    group_anws['num_grp_mbrs'] = []
    for key, val in group_anws.items():
        if val == num_mbrs:
            all_yes_sum += 1

print(total_group_sum)
print(all_yes_sum)
