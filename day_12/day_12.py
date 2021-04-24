with open('./day_12/input.txt') as doc:

    cur_line = doc.readline().replace('\n', '')
    print(cur_line)

    def parse_command(input_str):
        instruction = input_str[0]
        val = int(input_str[1:])

        return instruction, val

    ship_status = {
        'x': 0,
        'y': 0,
        # 0 if facing east [clock-wise so positive if left and neg if right]
        'dir_angle': 0
    }

    def apply_cmd_to_shp(ship_status, command):

        [inst, val] = parse_command(cur_line)

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

    while cur_line:
        print(cur_line)
        ship_status = apply_cmd_to_shp(ship_status, cur_line)
        print(ship_status)
        cur_line = doc.readline().replace('\n', '')

    manhattan_dist = abs(ship_status['x']) + abs(ship_status['y'])
    print(f'Answer Part 1: {manhattan_dist}')
