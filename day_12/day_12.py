with open('./day_12/input.txt') as doc:

    cur_line = doc.readline().replace('\n', '')
    print(cur_line)

    def parse_command(input_str):

        instruction = input_str[0]
        val = int(input_str[1:])

        return instruction, val

    # make ship object that we will change as commands come in
    ship_status = {
        'x': 0,
        'y': 0,
        # 0 if facing east [clock-wise so positive if left and neg if right]
        'dir_angle': 0
    }

    # apply command and update ship status
    def apply_cmd_to_shp(ship_status, inst, val):

        if inst == 'N':
            ship_status['y'] += val
        if inst == 'S':
            ship_status['y'] -= val
        if inst == 'E':
            ship_status['x'] += val
        if inst == 'W':
            ship_status['x'] -= val

        if inst == 'L':
            ship_status['dir_angle'] -= val
            ship_status['dir_angle'] = ship_status['dir_angle'] % 360

        if inst == 'R':
            ship_status['dir_angle'] += val
            ship_status['dir_angle'] = ship_status['dir_angle'] % 360

        if inst == 'F':
            cur_ship_dir_angle = ship_status['dir_angle']

            # kinda assuming can only turn this way
            if cur_ship_dir_angle == 0:
                ship_status['x'] += val

            if cur_ship_dir_angle == 90:
                ship_status['y'] -= val

            if cur_ship_dir_angle == 180:
                ship_status['x'] -= val

            if cur_ship_dir_angle == 270:
                ship_status['y'] += val

        return ship_status

    # part 2 functionality

    # make waypoint object that we will change as commands come in and units realtive to ship
    waypoint_status = {
        'x': 10,  # (east-west) relative to ship position
        'y': 1,  # (North-South)relative to ship position
    }

    ship_status_wwp = {
        'x': 0,
        'y': 0,
        # 0 if facing east [clock-wise so positive if left and neg if right]
        'dir_angle': 0
    }

    # apply command and update ship status
    def apply_wwp_cmd_to_shp_wwp(waypoint_status, ship_status, instruction_val):
        '''
            move ship in direction of waypoint
        '''
        ship_status['y'] += instruction_val*waypoint_status['y']
        ship_status['x'] += instruction_val*waypoint_status['x']

        return ship_status

   # apply command and update waypoint
    def apply_cmd_to_shp_and_wwp(waypoint_status, ship_status, inst, val):
        '''
            update waypoint information and move ship if needed
        '''
        if inst == 'N':
            waypoint_status['y'] += val
        if inst == 'S':
            waypoint_status['y'] -= val
        if inst == 'E':
            waypoint_status['x'] += val
        if inst == 'W':
            waypoint_status['x'] -= val

        if inst == 'L' or inst == 'R':
            waypoint_status = angle_tranform(waypoint_status, inst, val)

        # if forward then update ship status
        if inst == 'F':
            ship_status = apply_wwp_cmd_to_shp_wwp(
                waypoint_status, ship_status, val)

        return waypoint_status, ship_status

    def angle_tranform(waypoint_status, inst, val):
        '''
         apply 90 angle transform to the left or right
         for waypoint coordinates 
         https://en.wikipedia.org/wiki/Rotation_matrix
        '''

        num_90_rotations = int(val/90)
        print(num_90_rotations)
        for iteration_val in range(num_90_rotations):

            if inst == 'L':
                new_x = 0 + (-1 * waypoint_status['y'])
                new_y = waypoint_status['x']

                waypoint_status['x'] = new_x
                waypoint_status['y'] = new_y

            if inst == 'R':
                new_x = waypoint_status['y']
                new_y = 0 + (-1 * waypoint_status['x'])

                waypoint_status['x'] = new_x
                waypoint_status['y'] = new_y

        return waypoint_status

    while cur_line:

        # parse instructions
        [instruction, instruction_val] = parse_command(cur_line)

        # apply instructions directly to ship [part 1]
        ship_status = apply_cmd_to_shp(
            ship_status, instruction, instruction_val)

        # apply instructions to waypoint and then ship as needed [part 2]
        waypoint_status, ship_wwp_status = apply_cmd_to_shp_and_wwp(
            waypoint_status, ship_status_wwp, instruction, instruction_val)

        print(ship_status)
        print('wwp: ', ship_wwp_status)
        cur_line = doc.readline().replace('\n', '')

    # calculate manhatten distance for part 1 and part 2
    manhattan_dist = abs(ship_status['x']) + abs(ship_status['y'])
    manhattan_dist_wwb = abs(ship_wwp_status['x']) + abs(ship_wwp_status['y'])

    print(f'Answer Part 1: {manhattan_dist}')
    print(f'Answer Part 2: {manhattan_dist_wwb}')
