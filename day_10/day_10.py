with open('day_10/input.txt') as file_input:

    cur_line = file_input.readline()
    list_of_chargers = []
    while cur_line:
        list_of_chargers.append(int(cur_line))
        cur_line = file_input.readline()

    # check if they are unique
    # print(len(list_of_chargers))
    # print(sorted(list_of_chargers))

    #list_of_chargers = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    sorted_list = sorted(list_of_chargers)

    # add the charging outlet
    sorted_list.insert(0, 0)

    # add the device
    sorted_list.append(sorted_list[-1]+3)

    # calculate diffs
    diffs = [sorted_list[item_ind+1] - item for item_ind,
             item in enumerate(sorted_list[0:-1])]

    # now count the diffs
    diff_1_sum = 0
    diff_3_sum = 0
    for diff_val in diffs:
        if diff_val == 1:
            diff_1_sum += 1
        else:
            diff_3_sum += 1

    print(f'Part 1 Answer: {diff_1_sum*diff_3_sum} ')


# ok so part 2 is going to require recursion/// well you can try but it won't work...
'''
def find_num_adapters(input_num: int, target_voltage: int, adapter_list: list):

    num_successes = 0

    # enforce rule that can only connect to things up to 3 up
    search_voltage_list = range(input_num+1, input_num+3+1)

    # now search over this range
    for volt_val in search_voltage_list:

        # check if current range value is in provided adapter list
        if volt_val in adapter_list:

            # if it is in the list check if it is our target (voltage for device +3 of max in list)
            if volt_val == target_voltage:
                # if it is then add one to counter and return
                num_successes += 1
                return num_successes
            else:
                # if it is in the list but not the target then use recursion to continue down
                # the chain
                num_successes += find_num_adapters(
                    volt_val, target_voltage, adapter_list)
    # if nothing found then return zero (basecase)
    return num_successes


num_ways = find_num_adapters(1, 7, [5, 1, 7, 6, 4])

print(num_ways)

num_ways_2 = find_num_adapters(0, sorted_list[-1], sorted_list)

print(f'Answer for part 2 {num_ways_2}')
'''

# number of ways you can sum up to target num
# using all possible diffs?

# rule on chain of 1s if 3 ones then 4 possibilities
# if 2 ones then 2 possibilities
# final answer is sum of product of possiblities

# count number of ones!!!
# every subset of 3 continuous 1s can be rewritten as 4 differnt combinations
# every subset of 2 continuous 1s can be rewritten as 2 diff combos
# for sets of ones greater then ones count the subset of continuous pairs of 3s
# number of subset of threes is n-3+1
# make sure to count leftovers either a 1 or a two ones if two (or subtract them)
# then do as above finally multiply the counts to get total number


three_counts = []
cur_inds = 0
counting = True
while counting:

    # print(diff_val)
    cur_diff_val = diffs[cur_inds]

    if cur_diff_val == 1:
        counting_ind = 1
        while diffs[cur_inds+counting_ind] == 1:
            counting_ind += 1
        three_counts.append(counting_ind)
        cur_inds += counting_ind

    cur_inds += 1
    if cur_inds > len(diffs)-1:
        counting = False

# print(three_counts)

total_count = 1
for num_ones in three_counts:
    if num_ones > 1:

        if num_ones == 2:
            total_count *= 2
        elif num_ones == 3:
            total_count *= 4
        else:
            total_count *= (num_ones-3+1)*4 - (num_ones - (num_ones//3)*3)

print(f'Answer for part 2 {total_count}')
