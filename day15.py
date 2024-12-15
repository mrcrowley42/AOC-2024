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

def push_big_box():
    pass

for move in movelist:
    r, c = robot_position
    dy, dx = direction_map[move]
    r2, c2 = r + dy, c + dx
    if warehouse[r2][c2] == "#":
        continue
    if warehouse[r2][c2] in list('[]'):
        push_big_box()
        # can_move, locations = push_box(r2, c2, dy, dx, warehouse)
        # if not can_move:
        #     continue
        # lr, lc = locations
        # warehouse[lr][lc] = "O"
        # warehouse[r2][c2] = "."
    robot_position = (r2, c2)

print_warehouse(warehouse, robot_position)
print(gps_sum(warehouse, "["))