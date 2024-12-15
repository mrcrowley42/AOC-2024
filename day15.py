with open("inputs/day15_input.txt") as file:
    warehouse, movelist = file.read().split("\n\n")

# MAP DIRECTIONS TO VECTORS
direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
warehouse = [list(line) for line in warehouse.splitlines()]
movelist = "".join([line for line in movelist.splitlines()])

# FIND START POSITION OF ROBOT
def get_robot(grid):
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == "@":
                return (r, c)

def push_rock(r, c, dy, dx, warehouse):
    can_move = False
    while warehouse[r][c] == 'O':
        r, c = r + dy, c + dx
    if warehouse[r][c] == '.':
        can_move = True
    return can_move, (r, c)

# CLEAR ROBOT POSITION FROM WAREHOUSE
robot_position = get_robot(warehouse)
warehouse[robot_position[0]][robot_position[1]] = '.'

for move in movelist:

    # CHECK VISUAL
    print(move)
    # warehouse[robot_position[0]][robot_position[1]] = '@'
    # [print(''.join(line)) for line in warehouse]
    # warehouse[robot_position[0]][robot_position[1]] = '.'

    r, c = robot_position
    dy, dx = direction_map[move]
    r2, c2 = r + dy, c + dx
    if warehouse[r2][c2] == "#":
        continue
    if warehouse[r2][c2] == "O":
        can_move, locations = push_rock(r2, c2, dy, dx, warehouse)
        if not can_move:
            continue

        lr, lc = locations
        warehouse[lr][lc] = "O"
        warehouse[r2][c2] = "."
    robot_position = (r2, c2)

# warehouse[robot_position[0]][robot_position[1]] = '@'
# [print(''.join(line)) for line in warehouse]
# warehouse[robot_position[0]][robot_position[1]] = '.'

# GET SCORES