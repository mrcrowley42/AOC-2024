with open("inputs/day10_input.txt") as file:
    grid = [list(map(int, line)) for line in file.read().splitlines()]

offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
heads = [[r, c] for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]


def get_score(location, distinct=False):
    trails = 0
    locations = [location]
    visited = {(location[0], location[1])}

    while locations:
        r, c = locations.pop()
        value = grid[r][c]
        if value == 9:
            trails += 1
        for dx, dy in offsets:
            r2 = r + dx
            c2 = c + dy

            if not ( 0 <= r2 < len(grid) and 0 <= c2 < len(grid[0])):
                continue
            if grid[r2][c2] != value + 1:
                continue
            if (r2, c2) not in visited:
                locations.append([r2, c2])
            if distinct:
                continue
            
            visited.add((r2, c2))

    return trails

print(sum([get_score(location) for location in heads]))
print(sum([get_score(location, distinct=True) for location in heads]))