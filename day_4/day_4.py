import re


def passport_dict_generator():

    with open('day_4/input.txt') as it:

        cur_line = it.readline()
        pass_collection = []
        while cur_line:

            if len(cur_line) < 2:

                # going to be analyzing a complete pass

                yield pass_dict
                # pass_collection.append(pass_dict)

                # clear pass once analysis is done
                pass_dict = {}

            else:
                cur_line_split = cur_line.split(' ')
                for val in cur_line_split:
                    val_split = val.split(':')
                    try:
                        pass_dict[val_split[0]] = val_split[1].replace(
                            '\n', '')
                    except:
                        pass_dict = {}
                        pass_dict[val_split[0]] = val_split[1].replace(
                            '\n', '')

            cur_line = it.readline()

            # print(pass_dict)

        yield pass_dict


'''
part 1 block

passport_gen = passport_dict_generator()
valid_count = 0
for passport in passport_gen:
    print(passport)
    pass_key_list = list(passport)
    print(len(pass_key_list))
    if len(pass_key_list) == 8:

        valid_count += 1

    elif len(pass_key_list) < 7:
        continue
    else:
        if 'cid' in pass_key_list:
            continue
        else:
            valid_count += 1
print(valid_count)

'''

'''
 Part 2 Block
'''


def byr_filter(byr_val):

    if byr_val < 1920 or byr_val > 2002:
        return True
    else:
        return False


def iyr_filter(iyr_val):

    if iyr_val < 2010 or iyr_val > 2020:
        return True
    else:
        return False


def eyr_filter(eyr_val):

    if eyr_val < 2020 or eyr_val > 2030:
        return True
    else:
        return False


def hgt_filter(hgt_val_in):

    if hgt_val_in.count('cm') > 0:

        hgt_val = int(hgt_val_in[:-2])

        if hgt_val < 150 or hgt_val > 193:
            return True
        else:
            return False

    elif hgt_val_in.count('in') > 0:
        hgt_val = int(hgt_val_in[:-2])

        if hgt_val < 59 or hgt_val > 76:
            return True
        else:
            return False

    else:
        return True


def hcl_filter(hcl_val):

    if hcl_val[0] != '#' or len(hcl_val) != 7:
        return True
    else:

        matches = re.findall("[a-f,0-9]", hcl_val)
        if len(matches) < 6:
            return True
        else:
            return False


def ecl_filter(ecl_val):
    valid_ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if ecl_val in valid_ecl_list:
        return False
    else:
        return True


def pid_filter(pid_val):

    if len(pid_val) != 9:
        return True
    else:
        try:
            pid_val_int = int(pid_val)
            return False
        except:
            return True


def run_filters(passport_data):

    filter_dat = False
    byr_val = int(passport_data['byr'])
    iyr_val = int(passport_data['iyr'])
    eyr_val = int(passport_data['eyr'])
    hgt_val = passport_data['hgt']
    hcl_val = passport_data['hcl']
    ecl_val = passport_data['ecl']
    pid_val = passport_data['pid']

    if byr_filter(byr_val):
        filter_dat = True
        print('byr_fail')
    if iyr_filter(iyr_val):
        filter_dat = True
        print('iyr_fail')
    if eyr_filter(eyr_val):
        filter_dat = True
        print('eyr_fail')

    if hgt_filter(hgt_val):
        filter_dat = True
        print('hgt_fail')

    if hcl_filter(hcl_val):
        filter_dat = True
        print('hcl_fail')

    if ecl_filter(ecl_val):
        filter_dat = True
        print('ecl_fail')

    if pid_filter(pid_val):
        filter_dat = True
        print('pid_fail')

    return filter_dat


passport_gen = passport_dict_generator()
valid_count = 0
for passport in passport_gen:

    print(passport)
    pass_key_list = list(passport)

    if len(pass_key_list) == 8:

        if run_filters(passport):
            continue

        print('pass')
        valid_count += 1

    elif len(pass_key_list) < 7:
        print('fail')
        continue
    else:
        if 'cid' in pass_key_list:
            print('fail')
            continue
        else:
            if run_filters(passport):
                continue
            print('pass')
            valid_count += 1

print(valid_count)
