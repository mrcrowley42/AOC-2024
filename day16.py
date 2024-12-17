import heapq 
from collections import 

with open("inputs/day16_input.txt") as file:
    maze = [list(line) for line in file.read().splitlines()]

direction_map = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

def get_neighbours(r, c):
    neighbours = []
    for deg, offset in direction_map.items():
        dy, dx = offset
        r2, c2 = r + dy, c + dx
        if maze[r2][c2] != '#':
            neighbours.append((r2, c2, deg))
    return neighbours

def find_start_end(maze):
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if value == 'S':
                start = (r, c)
            if value == 'E':
                end = (r, c)

    return start, end

start, end = find_start_end(maze)
r, c = start
direction = 90
visited = {(r, c, direction)}
queue = [(0 ,r, c, direction)]

while queue:
    score, r, c, direction = heapq.heappop(queue)
    visited.add((r, c, direction))
    if (r, c) == end:
        print(score)
        break
    for nr, nc, deg in get_neighbours(r, c):
        if (nr, nc, deg) in visited:
            continue
        diff = abs(deg - direction)
        turns = 0 if diff == 0 else 1
        new_score = score + 1 + ( turns * 1000)
 

        heapq.heappush(queue, (new_score ,nr, nc, deg))