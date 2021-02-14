

def parse_command(input_string):

    cmd_components = input_string.split(' ')

    action_val = int(cmd_components[1].replace('/n', ''))

    cmd_components[1] = action_val

    return cmd_components


with open('day_8/input.txt') as file_in:

    cur_line = file_in.readline()

    act_val_list = []
    while cur_line:
        print(cur_line)
        out_parts = parse_command(cur_line)
        print(out_parts)
        act_val_list.append(out_parts)

        cur_line = file_in.readline()

    print(act_val_list)

    action_ind_list = []
    repeated_action_flag = False
    current_action_ind = 0
    acc_counter = 0
    while not repeated_action_flag:

        # check if action has occured already
        if current_action_ind in action_ind_list:
            repeated_action_flag = True

        else:
            action_ind_list.append(current_action_ind)
            cur_act = act_val_list[current_action_ind]

            if cur_act[0] == 'acc':
                acc_counter += cur_act[1]
                current_action_ind += 1
            elif cur_act[0] == 'nop':
                current_action_ind += 1
            else:  # in case of jump
                current_action_ind += cur_act[1]

    print(acc_counter)
