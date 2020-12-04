
def tree_counter(down_step, right_step):
    '''
        tree_counter: function counts number of trees in journey specified 
        by down_step and right_step trajectories

        inputs:
            down_step: (int) number of steps down
            right_step: (int) number of steps right

    '''
    with open('input.txt') as fp:

        tree_cnt = 0
        line = fp.readline()
        total_steps_right = 1

        # read first line in
        cur_line = line.replace('\n', '')
        line_length = len(cur_line)

        # read in lines corresponding to down_step
        down_step_count = 0
        while down_step_count < down_step:
            line = fp.readline()
            down_step_count += 1

        while line:  # while valid line

            cur_line = line.replace('\n', '')
            total_steps_right += right_step
            cur_ind = (total_steps_right % line_length) - 1

            val_at_ind = cur_line[cur_ind]

            if val_at_ind == '#':
                tree_cnt += 1

            #print(cur_line, total_steps_right, cur_ind, val_at_ind, tree_cnt)

            down_step_count = 0
            while down_step_count < down_step:
                line = fp.readline()
                down_step_count += 1

    print(tree_cnt)

    return tree_cnt


# call counter for all journeys and take product
tree_count_product = tree_counter(
    1, 1) * tree_counter(1, 3) * tree_counter(1, 5) * tree_counter(1, 7) * tree_counter(2, 1)

print(tree_count_product)
