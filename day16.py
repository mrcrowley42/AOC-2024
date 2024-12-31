from time import time
from collections import defaultdict
import heapq

with open("inputs/day16_input.txt") as file:
    maze = [list(line) for line in file.read().splitlines()]

directions = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}


def get_neighbours(r, c, grid):
    neighbours = []
    for direction, offset in directions.items():
        dr, dc = offset
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == '#':
            continue
        neighbours.append((nr, nc, direction))

    return neighbours


def locate_start_end(maze):
    start = end = None
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if value == 'S':
                start = (r, c)
                if end:
                    return start, end
            if value == 'E':
                end = (r, c)
                if start:
                    return start, end


start, end = locate_start_end(maze)
r, c = start
direction = 90
queue = [(0, r, c, direction, ((r, c),))]
best_paths = []

best_score = float("inf")
def bs(): return best_score


visted = defaultdict(bs)
startt = time()
while queue and queue[0][0] <= best_score:
    score, r, c, direction, path = heapq.heappop(queue)
    if (r, c) == end:
        best_score = score
        best_paths.append(path)
        continue

    if score > visted[(r, c, direction)]:
        continue
    visted[(r, c, direction)] = score

    for nr, nc, new_direction in get_neighbours(r, c, maze):
        if (nr, nc) in path:
            continue
        new_score = score + 1001 if new_direction != direction else score + 1
        heapq.heappush(queue, (new_score, nr, nc,
                       new_direction, path + ((nr, nc),)))


positions = {(x, y) for path in best_paths for x, y in path}
print(len(positions))
print(time() - startt)
