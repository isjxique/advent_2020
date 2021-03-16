from copy import deepcopy

with open('./day_11/input.txt') as doc:

    cur_line = doc.readline().replace('\n', '')
    print(cur_line)

    def txt_to_int(input_char):
        if input_char == '.':
            return -1
        if input_char == 'L':
            return 0
        if input_char == '#':
            return 1

    data_array = []
    while cur_line:
        data_array.append([txt_to_int(cur_char) for cur_char in cur_line])
        cur_line = doc.readline().replace('\n', '')

    num_rows = len(data_array)
    num_cols = len(data_array[0])
    print(num_rows, num_cols)

    # define filter
    def seat_filter(seat_row, seat_col, data_array, filter_mode):

        num_rows = len(data_array)
        num_cols = len(data_array[0])

        cur_seat_val = data_array[seat_row][seat_col]
        if cur_seat_val == -1:
            return -1

        # indeces of seats to check around current seat
        seats_to_check_row = [seat_row-1, seat_row, seat_row+1]
        seats_to_check_col = [seat_col-1, seat_col, seat_col+1]

        surrounding_pixel_sum = 0
        for row_check in seats_to_check_row:
            for col_check in seats_to_check_col:

                # try to get values around current pixel if out of bound continue [negative values exist..]
                if row_check < 0 or col_check < 0:
                    continue

                if row_check > num_rows-1 or col_check > num_cols-1:
                    continue

                # ignore current seat
                if row_check == seat_row and col_check == seat_col:
                    continue

                chk_seat_val = data_array[row_check][col_check]

                # just ignore floor
                if chk_seat_val == -1 and filter_mode == 1:
                    continue

                # ignore floor and look for next seat in view
                if chk_seat_val == -1 and filter_mode == 2:

                    row_change = row_check-seat_row
                    col_change = col_check-seat_col
                    num_iters = 1
                    continue_check = True
                    while continue_check:
                        next_row_check = row_check + row_change*num_iters
                        next_col_check = col_check + col_change*num_iters
                        if next_row_check < 0 or next_col_check < 0:
                            break

                        if next_row_check > num_rows-1 or next_col_check > num_cols-1:
                            break

                        next_chk_seat_val = data_array[next_row_check][next_col_check]

                        if next_chk_seat_val == -1:
                            num_iters += 1
                        else:
                            continue_check = False
                            chk_seat_val = next_chk_seat_val

                    # wasn't able to find valid seat so just continue
                    if continue_check:
                        continue

                # sum up values +1 if filled +0 if empty
                surrounding_pixel_sum += chk_seat_val

        # rule 1 if empty and no filled seats around it fill it
        if cur_seat_val == 0:
            if surrounding_pixel_sum == 0:
                new_seat_val = 1
            else:
                new_seat_val = 0

        # rule 2 if filled but more than 3 (4 if mode 2) seats around it filled then empty it
        if cur_seat_val == 1 and filter_mode == 1:
            if surrounding_pixel_sum > 3:
                new_seat_val = 0
            else:
                new_seat_val = 1

        if cur_seat_val == 1 and filter_mode == 2:
            if surrounding_pixel_sum > 4:
                new_seat_val = 0
            else:
                new_seat_val = 1

        return new_seat_val

    # now run through data and iterate until convergence
    def filter_iterator(data_array, filter_mode):
        # filter_mode = 1  # for part 1

        continue_iterating = True
        while continue_iterating:
            new_arr = []
            num_changes = 0

            # loop over all seats in array
            for row_ind in range(num_rows):
                new_row = []
                for col_ind in range(num_cols):
                    # apply filter to seat
                    new_val = seat_filter(
                        row_ind, col_ind, data_array, filter_mode)
                    old_val = data_array[row_ind][col_ind]
                    # check if a change occured
                    if new_val != old_val:
                        num_changes += 1

                    # add new seat val to current row
                    new_row.append(new_val)
                # add row to seat array
                new_arr.append(deepcopy(new_row))

            # replace previous seat array state with new one
            data_array = deepcopy(new_arr)

            # print(data_array)
            #print('break here')
            # print(new_arr)
            # print(num_changes)

            # stop iterating if num of changes is zero
            if num_changes == 0:
                continue_iterating = False

        return data_array

    def sum_occupied_seats(input_array):
        num_rows = len(input_array)
        num_cols = len(input_array[0])

        occupied_seat_sum = 0
        for row_ind in range(num_rows):
            for col_ind in range(num_cols):
                seat_val = input_array[row_ind][col_ind]
                if seat_val == 1:
                    occupied_seat_sum += 1
        return occupied_seat_sum

    # solve part 1
    filter_mode = 1
    part_1_final_array = filter_iterator(data_array, filter_mode)
    occupied_seat_sum = sum_occupied_seats(part_1_final_array)
    print(f'Answer Part 1: {occupied_seat_sum}')

    # solve part 2
    filter_mode = 2
    part_2_final_array = filter_iterator(data_array, filter_mode)
    occupied_seat_sum = sum_occupied_seats(part_2_final_array)
    print(f'Answer Part 2: {occupied_seat_sum}')
