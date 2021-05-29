
with open('./day_13/input.txt') as doc:
    '''
       Load in data and process 
    '''

    # read in earliest depart time
    earliest_depart_time = doc.readline()
    earliest_depart_time = int(earliest_depart_time)
    print(earliest_depart_time)

    # read in bus ids
    bus_ids = doc.readline()
    print(bus_ids)
    bus_ids = bus_ids.replace('\n', '').rsplit(',')
    print(bus_ids)

    # remove invalid bus ids
    valid_bus_ids = [int(val) for val in bus_ids if val != 'x']
    print(valid_bus_ids)

    # figure out margin between earliest departure time and
    # the bus departure time for all valid buses
    margin_list = []
    for val in valid_bus_ids:

        # bus dpeart time just before earliest departure time
        min_match_time = (earliest_depart_time // val)*val

        # if it matches perfectly then margin is zeros
        if min_match_time == earliest_depart_time:
            margin = 0
        else:
            # if it doesn't match then wait until next departure and calculate margin
            margin = (earliest_depart_time // val) * \
                val + val - earliest_depart_time
        margin_list.append(margin)

        print(earliest_depart_time, val, earliest_depart_time //
              val, earliest_depart_time % val, margin)

    # now figure out which bus had the smallest departure time
    for val_num, val in enumerate(margin_list):
        if val == min(margin_list):
            min_ind = val_num
    best_bus_id = valid_bus_ids[min_ind]

    print('solution part 1: ', best_bus_id*margin_list[min_ind])

    '''
    # part 2 get min time at which each bus departs 1 minute apart
     note that I tried taking time steps according to first bus but
     this requires a lot of iterations, so can take steps according to larget
     valid bus id and well it still takes a lot of time. I am still working
     on solution that cuts down time or is closed form...
    '''

    # grab valid time offsets
    valid_time_offsets = [val for val, id in enumerate(bus_ids) if id != 'x']

    # pop out the bus id with larget value and use as time step
    largest_bus_id = max(valid_bus_ids)
    largest_bus_id_offset_ind = [offset_val_ind for offset_val_ind, id in enumerate(
        valid_bus_ids) if int(id) == largest_bus_id]
    largest_bus_id_offset = valid_time_offsets[largest_bus_id_offset_ind[0]]
    new_time_offsets = [offset_val-largest_bus_id_offset for offset_val,
                        id in zip(valid_time_offsets, valid_bus_ids) if id != largest_bus_id]
    new_valid_bus_ids = [
        bus_id for bus_id in valid_bus_ids if bus_id != largest_bus_id]

    search_min_time_val = True
    orig_bus_id = largest_bus_id  # int(bus_ids[0])
    cur_time = orig_bus_id  # orig_bus_id  # 69306185  # orig_bus_id
    iter_num = 0
    while search_min_time_val:

        # assume this is the one
        found_match_time = True
        for bus_id, time_offset in zip(new_valid_bus_ids, new_time_offsets):

            bus_time = int(bus_id)
            check_time = cur_time + time_offset
            if check_time % bus_time != 0:
                # if you find that it isn't then make it false
                #print('fail on', check_time, bus_time)
                found_match_time = False
                break

        # if you made it all the way then confirm
        if found_match_time:
            search_min_time_val = False
        else:
            # add time if didn't find the one
            cur_time += orig_bus_id
        iter_num += 1
        print(
            f'Iteration Num: {iter_num} fail on {bus_id} with time value {cur_time}')

    if largest_bus_id_offset_ind[0] == 0:
        print('solution part 2: ', cur_time)
    else:
        print('solution part 2: ', cur_time+new_time_offsets[0])
