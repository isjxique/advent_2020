
with open('input.txt') as file_in:

    cur_line = file_in.readline()

    while cur_line:
        print(cur_line)
        cur_line = file_in.readline()
