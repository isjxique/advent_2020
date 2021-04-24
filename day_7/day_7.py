import re

with open('day_7/input_t2.txt') as file_in:

    cur_line = file_in.readline()

    bag_collection = {}

    while cur_line:

        cur_line = cur_line.replace('\n', '')
        cur_line = cur_line.split('contain')
        cur_bag_name = cur_line[0][0:-2]

        # print(cur_bag_name)

        contained_bags = cur_line[1].split(',')
        for bag_val in contained_bags:

            trim_bag_val = bag_val[1:]

            search_for_num = re.search('[0-9]', trim_bag_val)
            search_for_bag_end = re.search('bag', trim_bag_val)

            if search_for_num is None:
                # print('none')
                bag_collection[cur_bag_name] = {}

            else:
                num_val = search_for_num.span()
                bag_val = search_for_bag_end.span()

                contained_bag_num = int(trim_bag_val[num_val[0]:num_val[1]])
                contained_bag_name = trim_bag_val[num_val[1]+1:bag_val[1]]

                # print(contained_bag_name)
                # print(contained_bag_num)
                if cur_bag_name in bag_collection:
                    bag_collection[cur_bag_name][contained_bag_name] = contained_bag_num
                else:
                    bag_collection[cur_bag_name] = {}
                    bag_collection[cur_bag_name][contained_bag_name] = contained_bag_num

        # print(bag_collection)
        cur_line = file_in.readline()

# print(bag_collection)


print(bag_collection['shiny gold bag'])

'''
# part 1
searching_all_bags = 1
bag_w_shiny_gb = []
cur_bags_to_search = []
new_bags_to_search = []
while searching_all_bags:

    if cur_bags_to_search == []:
        for key, value in bag_collection.items():
            if 'shiny gold bag' in value:
                new_bags_to_search.append(key)

    else:

        cur_bags_to_search = new_bags_to_search
        new_bags_to_search = []
        for bag in cur_bags_to_search:
            for key, value in bag_collection.items():
                if bag in value:
                    new_bags_to_search.append(key)
    cur_bags_to_search = new_bags_to_search
    if cur_bags_to_search == []:
        searching_all_bags = 0
    bag_w_shiny_gb.extend(new_bags_to_search)

# print(bag_w_shiny_gb)
print(len(bag_w_shiny_gb))
print(len(set(bag_w_shiny_gb)))
'''

# part 2


continue_search = 1
sum_of_contained_bags = 0
contained_bag_list = []
while continue_search:

    if contained_bag_list == []:

        for bag_name, num_bags_contained in bag_collection['shiny gold bag'].items():
            contained_bag_list.append(bag_name)
            sum_of_contained_bags += num_bags_contained

    else:

        process_bag_list = contained_bag_list
        contained_bag_list = []
        for bag_name in process_bag_list:

            for bag_name, num_bags_contained in bag_collection[bag_name].items():
                contained_bag_list.append(bag_name)
                sum_of_contained_bags += num_bags_contained

    if contained_bag_list == []:
        continue_search = 0

print('num contained:')
print(sum_of_contained_bags)


def recursive_count(in_bag, in_val, bag_collection):

    in_bag_list = list(in_bag)
    if in_bag == {}:
        return in_val
    else:

        smaller_bag = in_bag
        in_val_sub = in_bag[in_bag_list[0]]*in_val
        del smaller_bag[in_bag_list[0]]
        count_1 = recursive_count(
            bag_collection[in_bag_list[0]], in_val_sub, bag_collection)
        count_2 = recursive_count(smaller_bag, in_val, bag_collection)

        return count_1+count_2


def count_contained_bags(in_bag, in_val, bag_collection):

    in_bag_list = list(in_bag)
    if in_bag == {}:
        return in_val

    else:
        sum_of_contained_bags = 0
        for bag_name in in_bag_list:
            in_val_sub = in_bag[bag_name]*in_val

            count_1 = recursive_count(
                bag_collection[bag_name], in_val_sub, bag_collection)

            sum_of_contained_bags += count_1

        return sum_of_contained_bags


"""
sum_of_contained_bags = 0
for bag_name, num_bags_contained in bag_collection['shiny gold bag'].items():
    contained_bag_list.append(bag_name)
    sub_bag_count = recursive_count(
        bag_collection[bag_name], num_bags_contained, bag_collection)
    sum_of_contained_bags += sub_bag_count

print(sum_of_contained_bags)
"""

'''
sum_of_contained_bags = 0
for bag_name, num_bags_contained in bag_collection['shiny gold bag'].items():
    contained_bag_list.append(bag_name)
    sub_bag_count = count_contained_bags(
        bag_collection[bag_name], num_bags_contained, bag_collection)
    sum_of_contained_bags += sub_bag_count + num_bags_contained

print(sum_of_contained_bags)

'''


def count_bags(bag_type):
    return 1 + sum(int(number)*count_bags(colour) for colour, number in bag_collection[bag_type].items())


print("Part 2: " + str(count_bags("shiny gold bag")-1))
