from itertools import product

with open('./day_14/input.txt') as doc:
    cur_line = doc.readline()

    def parse_mask_line(input_line):
        '''
         - parses a mask line 
         - returns mask binary string
        '''

        cur_parse_line = input_line.split(' ')
        # print(cur_parse_line)
        mask_val = cur_parse_line[2].replace('\n', '')

        return mask_val

    def parse_mem_line(input_line):
        '''
        - parses a memory command line
        - returns address (str) of binary value and binary value (str) at that address 
        '''

        cur_parse_line = input_line.split(' ')
        # print(cur_parse_line)

        # grab memory address
        mem_address = cur_parse_line[0].split('[')
        mem_address = mem_address[1][:-1]

        # get value and encode to binary string
        mem_value = bin(
            int(cur_parse_line[2].replace('\n', ''))).replace('0b', '')

        # pad mask as needed
        mem_val_len = len(mem_value)
        mem_val_pad_len = 36-mem_val_len
        mem_val_padding = '0'*mem_val_pad_len
        mem_value = mem_val_padding + mem_value

        return mem_address, mem_value

    print(cur_line)

    def apply_mask_to_val(mask, value):
        '''
        - Applies mask to in-memory value 
        - Returns the masked value
        '''

        masked_value = ''
        for mask_val, value_val in zip(mask, value):
            if mask_val == 'X':
                masked_value += value_val
            else:
                masked_value += mask_val

        return masked_value

    def apply_mask_to_address(mask, address):
        '''
        - Applies mask to in-memory value 
        - Returns list of addresses
        '''

        # get address and encode to binary string
        address_bin = bin(int(address)).replace('0b', '')

        # pad address as needed
        address_len = len(address_bin)
        address_pad_len = 36-address_len
        address_padding = '0'*address_pad_len
        address_bin = address_padding + address_bin

        # apply mask
        masked_value = ''
        num_floats = 0
        for mask_val, add_val in zip(mask, address_bin):
            if mask_val == '0':
                masked_value += add_val
            else:
                masked_value += mask_val

            if mask_val == 'X':
                num_floats += 1

        # now will make list of addresses
        address_list = []

        # get all possible values to replace x by
        fill_vals = [0, 1]
        all_fill_vals = product(fill_vals, repeat=num_floats)

        # now for each combination replace x
        for fill_comb in all_fill_vals:

            new_address = ''
            cur_fill_val_indx = 0
            for address_val in masked_value:
                if address_val == 'X':
                    new_address += str(fill_comb[cur_fill_val_indx])
                    cur_fill_val_indx += 1
                else:
                    new_address += address_val

            # add newly computed address to list
            new_address = str(int(new_address, 2))
            address_list.append(new_address)

        return address_list

    def sum_of_vals_in_memory(memory_dict):

        running_sum = 0
        for key, value in memory_dict.items():

            running_sum += int(value, 2)

        return running_sum

    mem_dict = {}
    mem_dict_part_2 = {}
    while cur_line:

        is_mask = cur_line.find('mask')
        if is_mask != -1:
            cur_mask = parse_mask_line(cur_line)

        is_mem = cur_line.find('mem')
        if is_mem != -1:
            cur_mem_address, cur_mem_value = parse_mem_line(cur_line)

            # part 1
            masked_val = apply_mask_to_val(cur_mask, cur_mem_value)
            mem_dict[cur_mem_address] = masked_val

            # part 2 work
            address_list = apply_mask_to_address(cur_mask, cur_mem_address)
            # now fill in cur memory value at all the address
            for address in address_list:
                mem_dict_part_2[address] = cur_mem_value

        cur_line = doc.readline()

    # part 1
    running_sum = sum_of_vals_in_memory(mem_dict)
    print(f'Answer Part 1: {running_sum}')

    # part 2
    running_sum_p2 = sum_of_vals_in_memory(mem_dict_part_2)
    print(f'Answer Part 1: {running_sum_p2}')
