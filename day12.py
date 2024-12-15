with open("inputs/day12_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]

positions_to_check = {(r, c) for r, row in enumerate(input) for c, value in enumerate(row)}
offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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

    for location in visited:
        if location in positions_to_check:
            positions_to_check.remove(location)

    return len(visited) * edges

total = 0
while positions_to_check:
    location = positions_to_check.pop()
    total += get_score(location, input)
    
print(total)