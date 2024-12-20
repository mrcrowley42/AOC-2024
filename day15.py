from time import time as tt


def gps_sum(warehouse, box_symbol):
    total_score = 0
    for r, row in enumerate(warehouse):
        for c, value in enumerate(row):
            if value == box_symbol:
                total_score += 100 * r + c

    return total_score


def get_robot(grid):
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == "@":
                return (r, c)


def print_warehouse(warehouse, r, c):
    warehouse[r][c] = '@'
    [print(''.join(line)) for line in warehouse]
    warehouse[r][c] = '.'


def push_box(r, c, dr, dc, warehouse):
    targets = []
    r += dr
    c += dc
    targets.append((r, c))
    can_move = False
    if warehouse[r][c] == "#":
        return can_move, targets

    while warehouse[r][c] == 'O':
        r += dr
        c += dc
        targets.append((r, c))

    if warehouse[r][c] == '.':
        can_move = True

    return can_move, targets


direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
replacements = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}

with open("inputs/day15_input.txt") as file:
    warehouse, movelist = file.read().split("\n\n")

warehouse = [list(line) for line in warehouse.splitlines()]
movelist = "".join([line for line in movelist.splitlines()])

og_warehouse = [list(row) for row in warehouse]
startt = tt()

r, c = get_robot(warehouse)
warehouse[r][c] = '.'

for move in movelist:
    dr, dc = direction_map[move]
    can_move, targets = push_box(r, c, dr, dc, warehouse)
    if not can_move:
        continue
    tr, tc = targets[::-1][0]
    warehouse[tr][tc] = "O"
    r += dr
    c += dc
    warehouse[r][c] = "."


# print(gps_sum(warehouse, "O"))

warehouse = [list("".join(replacements[value] for value in row)) for row in og_warehouse]
r, c = get_robot(warehouse)
warehouse[r][c] = '.'


def push_big_box(r, c, dr, dc, warehouse):
    targets = []
    targets.append((r, c))
    can_move = True

    for tr, tc in targets:
        nr = tr + dr
        nc = tc + dc
        if warehouse[nr][nc] == "#":
            return False, []
        if (nr, nc) in targets:
            continue
        if warehouse[nr][nc] == "[":
            targets.append((nr, nc))
            targets.append((nr, nc +1))
        
        if warehouse[nr][nc] == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))

    return can_move, targets


for move in movelist:
    dr, dc = direction_map[move]
    can_move, targets = push_big_box(r, c, dr, dc, warehouse)
    if not can_move:
        continue
    copy = [list(row) for row in warehouse]
    for tr, tc in targets:
        warehouse[tr][tc] = "."

    for tr, tc in targets:
        warehouse[tr + dr][tc + dc] = copy[tr][tc]
    r += dr
    c += dc
    warehouse[r][c] = "."
    # print_warehouse(warehouse, r, c)


print(gps_sum(warehouse, "["))

# def push_big_box_vertical(r, c, dy, warehouse):
#     can_move = True
#     offset = -1 if warehouse[r][c] == "]" else 1
#     locations = []
#     # warehouse[r][c] = '.'
#     # warehouse[r][c+offset] = '.'
#     locations = [[r, c], [r, c+ offset]]
#     to_check = [[r, c], [r, c+ offset]]

#     while to_check:
#         r, c = to_check.pop()
#         r2, c2 = r + dy, c + dx

#         if warehouse[r2][c2] == "#":
#             can_move = False
#             break

#         elif warehouse[r2][c2] == warehouse[r][c]:
#             to_check.append([r2, c2])
#             locations.append([r2, c2])

#         elif warehouse[r2][c2] == "]" and warehouse[r][c] == "[":
#             to_check.append([r2, c2])
#             to_check.append([r2, c2 - 1])
#             locations.append([r2, c2 -1])
#             locations.append([r2, c2])

#         elif warehouse[r2][c2] == "[" and warehouse[r][c] == "]":
#             to_check.append([r2, c2])
#             to_check.append([r2, c2 + 1])
#             locations.append([r2, c2 + 1])
#             locations.append([r2, c2])

#         else:

#             locations.append([r2, c2])


#     return can_move, locations


# def push_big_box_sideways(r, c, dx, warehouse):
#     can_move = False
#     locations = []

#     if move in list('<>'):
#         while warehouse[r][c] in list('[]'):
#             r, c = r + dy, c + dx
#             locations.append([r, c])
#         if warehouse[r][c] == '.':
#             can_move = True

#     return can_move, locations

# print_warehouse(warehouse, robot_position)
# for move in movelist[:-2]:
#     r, c = robot_position
#     dy, dx = direction_map[move]
#     r2, c2 = r + dy, c + dx
#     if warehouse[r2][c2] == "#":
#         continue
#     if warehouse[r2][c2] in list('[]'):
#         if move in list("><"):
#             can_move, locations = push_big_box_sideways(r2, c2, dx, warehouse)
#             if not can_move:
#                 continue
#             direction = 1 if move == '<' else -1
#             old_row = [x for x in warehouse[r]]
#             for i in range(len(locations)):
#                 warehouse[r][locations[i][1]
#                              ] = old_row[locations[i][1]+direction]
#             warehouse[r2][c2] = "."
#         else:
#             can_move, locations = push_big_box_vertical(r2, c2, dy, warehouse)
#             if not can_move:
#                 continue
#             old_warehouse = list([list(x) for x in warehouse])
#             gg = list([list(x) for x in warehouse])
#             print(locations)
#             for location in locations:
#                 r3, c3 = location
#                 gg[r3][c3] = "x"
#                 warehouse[r3][c3] = old_warehouse[r3+-dy][c3]

#             if warehouse[r2+dy][c2] == "[":
#                 warehouse[r2][c2+1] = "."

#             if warehouse[r2+dy][c2] == "]":
#                 warehouse[r2][c2-1] = "."
#             warehouse[r2][c2] = "."


#             # [print(''.join(line)) for line in gg]
#     robot_position = (r2, c2)
#     print(move)
#     print_warehouse(warehouse, robot_position)


# print(gps_sum(warehouse, "["))
