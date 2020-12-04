'''
with open('input.txt') as fp:

    line = fp.readline()
    cnt = 0

    while line:

        split_line = line.split(' ')

        min_max_vals = [int(num_val) for num_val in split_line[0].split('-')]
        letter_to_match = split_line[1][0]
        string_to_search = split_line[2].replace('\n', '')

        num_occ = split_line[2].count(letter_to_match)

        print("Line {}: {}".format(cnt, line.split(' ')))
        print(min_max_vals, letter_to_match, string_to_search, num_occ)

        if num_occ <= min_max_vals[1] and num_occ >= min_max_vals[0]:
            cnt += 1

        line = fp.readline()

print(cnt)

'''

with open('input.txt') as fp:

    line = fp.readline()
    cnt = 0

    while line:  # while valid line

        split_line = line.split(' ')

        min_max_vals = [int(num_val) for num_val in split_line[0].split('-')]
        letter_to_match = split_line[1][0]
        string_to_search = split_line[2].replace('\n', '')

        try:
            first_letter = string_to_search[min_max_vals[0]-1]
            second_letter = string_to_search[min_max_vals[1]-1]

        except:
            continue

        first_match = 1 if first_letter == letter_to_match else 0
        second_match = 1 if second_letter == letter_to_match else 0

        if (first_match+second_match) == 1:
            cnt += 1

        line = fp.readline()


print(cnt)
