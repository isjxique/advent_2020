
from itertools import product, islice

with open('day_9/input.txt') as input_txt:

    # check grab first 25 items
    preamble_list = []
    num_preamble = 25
    ii = 0
    while ii < num_preamble:
        cur_line = input_txt.readline()
        preamble_list.append(int(cur_line))
        ii += 1

    # now load the next item and check if it is sum of previous 25 items
    # if it is load in next item and stop if it is not sum
    in_sum_list = True
    while in_sum_list:

        # get all sums of previous 25 items
        sum_list = [x+y for x in preamble_list for y in preamble_list]

        # read in next value
        cur_line = input_txt.readline()
        cur_val_int = int(cur_line)

        # check if value is in list of possible sums
        if cur_val_int in sum_list:
            # if it is then remove the first item in list and append current item
            # pop out first item
            preamble_list.pop(0)
            # add new value
            preamble_list.append(cur_val_int)

        else:
            # if not then print value
            print(f'Answer Part 1: {cur_val_int}')
            final_val = cur_val_int

            in_sum_list = False


with open('day_9/input.txt') as input_txt:

    # check grab first 25 items
    val_list = []
    ii = 0
    cur_line = input_txt.readline()
    while cur_line:
        val_list.append(int(cur_line))
        cur_line = input_txt.readline()

    print(len(val_list))


def make_sublists(input_list, sub_list_len):
    """


    """
    sublist = []

    input_list_len = len(input_list)

    for jj in range(input_list_len-sub_list_len):
        sublist.append(input_list[jj:jj+sub_list_len])

    return sublist


for kk in range(2, len(val_list)+1):
    sub_lists = make_sublists(val_list, kk)

    for sub_list in sub_lists:
        cur_sum = sum(sub_list)
        if cur_sum == final_val:
            print('did it')
            #print(min(sub_list), max(sub_list), min(sub_list) + max(sub_list))
            key_sum = min(sub_list) + max(sub_list)
            print(f'Answer part 2: {key_sum}')
