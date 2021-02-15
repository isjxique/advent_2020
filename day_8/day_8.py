
import copy


def parse_command(input_string):
    """

    """
    cmd_components = input_string.split(' ')
    action_val = int(cmd_components[1].replace('/n', ''))
    cmd_components[1] = action_val

    return cmd_components


def process_command_list(command_list):
    """

    """

    action_ind_list = []
    repeated_action_flag = False
    current_action_ind = 0
    acc_counter = 0
    while not repeated_action_flag:

        # check if action has occured already
        if current_action_ind in action_ind_list:
            repeated_action_flag = True

        elif current_action_ind == len(command_list):
            return acc_counter, repeated_action_flag

        else:
            action_ind_list.append(current_action_ind)
            cur_act = command_list[current_action_ind]

            if cur_act[0] == 'acc':
                acc_counter += cur_act[1]
                current_action_ind += 1
            elif cur_act[0] == 'nop':
                current_action_ind += 1
            else:  # in case of jump
                current_action_ind += cur_act[1]

    return acc_counter, repeated_action_flag


with open('day_8/input.txt') as file_in:

    cur_line = file_in.readline()

    act_val_list = []
    test_ind_list = []
    cur_list_ind = 0
    while cur_line:

        # parse line and add to command list
        out_parts = parse_command(cur_line)
        act_val_list.append(out_parts)

        # add command index to list for testing if it is
        # acc or jmp (so not nop)

        if out_parts[0] != 'acc':
            test_ind_list.append(cur_list_ind)

        # grab new line
        cur_line = file_in.readline()
        cur_list_ind += 1

    # print(act_val_list)

    # get acc
    acc_counter, repeat_flag = process_command_list(act_val_list)
    print('part 1 solution: ', acc_counter)

    # Part 2

    for inspect_ind in test_ind_list:
        # make copy of list (need a deep copy!!)
        #act_val_list_copy = copy.deepcopy(act_val_list)
        #act_val_list_copy = act_val_list[:]
        act_val_list_copy = [copy.deepcopy(val) for val in act_val_list].copy()

        # switch command in list
        cmd_at_cur_ind = act_val_list[inspect_ind][0]
        if cmd_at_cur_ind == 'nop':
            act_val_list_copy[inspect_ind][0] = 'jmp'
        else:
            act_val_list_copy[inspect_ind][0] = 'nop'

        # no process this list
        acc_counter, repeat_flag = process_command_list(act_val_list_copy)

        # if not infinite then note value
        if repeat_flag == False:
            print('Part 2 Solution: ', acc_counter)
            break
