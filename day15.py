from copy import deepcopy

with open("inputs/day15_input.txt") as file:
    warehouse, movelist = file.read().split("\n\n")

def gps_sum(warehouse, box_symbol):
    total_score = 0 
    for r, row in enumerate(warehouse):
        for c, value in enumerate(row):
            if value == box_symbol:
                total_score += (100 * r) + c
    
    return total_score

def enlarge_warehouse(warehouse):
    replacements = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    large_warehouse = []
    for row in warehouse:
        new_row = ""
        for value in row:
            new_row += replacements[value]
        large_warehouse.append(list(new_row))
    return large_warehouse

def get_robot(grid):
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == "@":
                return (r, c)

def push_box(r, c, dy, dx, warehouse):
    can_move = False
    while warehouse[r][c] == 'O':
        r, c = r + dy, c + dx
    if warehouse[r][c] == '.':
        can_move = True
    return can_move, (r, c)

def push_big_box_vertical(r, c, dy, warehouse):
    can_move = False
    locations = []
    offset = -1 if warehouse[r][c] == "]" else 1
    while warehouse[r][c] in list('[]') and warehouse[r][c+offset] in list('[]'):
        r, c = r + dy, c + dx
        locations.append([[r, c], [r, c + offset]])
    if warehouse[r][c] == warehouse[r][c+offset] == '.':
        can_move = True
    return can_move, locations

def push_big_box_sideways(r, c, dx, warehouse):
    can_move = False
    locations = []

    if move in list('<>'):
        while warehouse[r][c] in list('[]'):
            r, c = r + dy, c + dx
            locations.append([r, c])
        if warehouse[r][c] == '.':
            can_move = True

    return can_move, locations

def print_warehouse(warehouse, robot_position):
    warehouse[robot_position[0]][robot_position[1]] = '@'
    [print(''.join(line)) for line in warehouse]
    # warehouse[robot_position[0]][robot_position[1]] = '.'

# MAP DIRECTIONS TO VECTORS
direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
warehouse = [list(line) for line in warehouse.splitlines()]
movelist = "".join([line for line in movelist.splitlines()])
og_warehouse = deepcopy(warehouse)

# CLEAR ROBOT POSITION FROM WAREHOUSE
robot_position = get_robot(warehouse)
warehouse[robot_position[0]][robot_position[1]] = '.'

for move in movelist:
    r, c = robot_position
    dy, dx = direction_map[move]
    r2, c2 = r + dy, c + dx
    if warehouse[r2][c2] == "#":
        continue
    if warehouse[r2][c2] == "O":
        can_move, locations = push_box(r2, c2, dy, dx, warehouse)
        if not can_move:
            continue
        lr, lc = locations
        warehouse[lr][lc] = "O"
        warehouse[r2][c2] = "."
    robot_position = (r2, c2)

# PART 1
print_warehouse(warehouse, robot_position)
print(gps_sum(warehouse, "O"))

# PART 2 
# BUILD BIGGER WAREHOUSE
warehouse = enlarge_warehouse(og_warehouse)
robot_position = get_robot(warehouse)
warehouse[robot_position[0]][robot_position[1]] = '.'

for move in movelist:
    r, c = robot_position
    dy, dx = direction_map[move]
    r2, c2 = r + dy, c + dx
    if warehouse[r2][c2] == "#":
        continue
    if warehouse[r2][c2] in list('[]'):
        if move in list("><"):
            can_move, locations = push_big_box_sideways(r2, c2, dx, warehouse)
            if not can_move:
                continue
            direction = 1 if move == '<' else -1
            old_row = [x for x in warehouse[r]]
            for i in range(len(locations)):
                warehouse[r][locations[i][1]] = old_row[locations[i][1]+direction]
            warehouse[r2][c2] = "."
        else:
            can_move, locations = push_big_box_vertical(r2, c2, dy, warehouse)
            if not can_move:
                continue
            direction = 1 if move == '^' else -1
            old_cols = list(map(list, zip(*warehouse)))
            old_columns = [old_cols[c], old_cols[locations[0][1][1]]]
            for j in range(2):
                old = old_columns[j]
                print("".join(old))
                # for i in range(len(locations)):
                #     warehouse[r][locations[i][1]] = old_row[locations[i][1]+direction]
                #     print(locations[i])

            warehouse[r2][c2] = "."
           
    robot_position = (r2, c2)

print_warehouse(warehouse, robot_position)
print(gps_sum(warehouse, "["))