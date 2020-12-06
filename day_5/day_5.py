import re


def line_generator():

    with open('day_5/input.txt') as in_file:

        cur_line = in_file.readline()

        while cur_line:
            cur_line = cur_line.replace('/n', '')

            yield cur_line

            cur_line = in_file.readline()


def traverse_seat_list(cur_pass, min_letter, max_letter, seat_list):

    for let_num in range(min_letter, max_letter):

        #print(let_num, cur_pass[let_num])
        get_cur_num_rows = len(seat_list)

        if cur_pass[let_num] == 'F' or cur_pass[let_num] == 'L':
            seat_list = seat_list[0:get_cur_num_rows//2]
        else:
            seat_list = seat_list[get_cur_num_rows//2:]

    return seat_list[0]


def process_pass(cur_pass):
    cur_pass = cur_pass.replace('\n', '')

    len_of_pass = len(cur_pass)
    # print(len_of_pass)
    num_rows = 128
    num_cols = 8

    row_list = list(range(num_rows))
    col_list = list(range(num_cols))

    row_num = traverse_seat_list(cur_pass, 0, 7, row_list)
    col_num = traverse_seat_list(cur_pass, 7, 10, col_list)
    #print(row_num, col_num)

    return row_num, col_num


# start boarding pass generator
boarding_pass_gen = line_generator()

# find highest boarding pass id and make list of ids
highest_p_pass_id = 0
pass_id_list = []
for b_pass in boarding_pass_gen:
    # print(b_pass)
    row, col = process_pass(b_pass)
    cur_pass_id = 8*row + col
    pass_id_list.append(cur_pass_id)
    if cur_pass_id > highest_p_pass_id:
        highest_p_pass_id = cur_pass_id

print(highest_p_pass_id)

# sort list of ids and find your own as the one in between gap
pass_id_list = sorted(pass_id_list)
prev_val = pass_id_list[0]
for val in pass_id_list[1:]:
    cur_diff = val - prev_val
    if cur_diff > 1:
        print(val, prev_val)
    prev_val = val
