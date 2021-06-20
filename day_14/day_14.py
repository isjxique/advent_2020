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

    def sum_of_vals_in_memory(memory_dict):

        running_sum = 0
        for key, value in memory_dict.items():

            running_sum += int(value, 2)

        return running_sum

    mem_dict = {}
    while cur_line:

        is_mask = cur_line.find('mask')
        if is_mask != -1:
            cur_mask = parse_mask_line(cur_line)

        is_mem = cur_line.find('mem')
        if is_mem != -1:
            cur_mem_address, cur_mem_value = parse_mem_line(cur_line)
            masked_val = apply_mask_to_val(cur_mask, cur_mem_value)
            mem_dict[cur_mem_address] = masked_val

        cur_line = doc.readline()
        print(cur_line)

    running_sum = sum_of_vals_in_memory(mem_dict)

    print(f'Answer Part 1: {running_sum}')
