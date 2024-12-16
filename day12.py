with open("inputs/day12_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]

positions_to_check = {(r, c) for r, row in enumerate(input) for c, value in enumerate(row)}
offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

compass = {0: (-1, 0), 45: (-1, 1), 90: (0, 1), 135: (1, 1), 180: (1, 0), 225: (1, -1), 270: (0, -1), 315: (-1, -1), 360: (-1, 0)}


def offset(a, b):
    r1, c1 = a
    r2, c2 = b

    return (r1 + r2, c1 + c2)


def is_corner(locations, a1, a2, d):
    return ((a1 in locations and a2 in locations) and d not in locations) or (a1 not in locations and a2 not in locations)

def get_corners(locations, grid):
    corners = 0
    for location in locations:
        for i in range(4):
            if is_corner(locations, offset(location, compass[0+(i*90)]),offset(location, compass[90+(90*i)]) , offset(location, compass[45 + (90*i)])):
                corners += 1

    return corners

def get_score(location, grid):
    start_value = grid[location[0]][location[1]]
    locations = [location]
    visited = {(location[0], location[1])}
    edges = 0
    while locations:
        r, c = locations.pop()
        for dx, dy in offsets:
            r2 = r + dx
            c2 = c + dy
            if not ( 0 <= r2 < len(grid) and 0 <= c2 < len(grid[0])):
                edges += 1
                continue
            if grid[r2][c2] != start_value:
                edges += 1
                continue
            if (r2, c2) not in visited:
                locations.append([r2, c2])
                visited.add((r2, c2))

    corners = get_corners(visited, grid)
    for location in visited:
        if location in positions_to_check:
            positions_to_check.remove(location)
    print(start_value, corners)
    # return len(visited) * edges
    return len(visited) * corners

total = 0
while positions_to_check:
    location = positions_to_check.pop()
    total += get_score(location, input)
    
print(total)