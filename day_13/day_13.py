
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
