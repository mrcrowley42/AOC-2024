import heapq

with open("inputs/day16_input.txt") as file:
    maze = [list(line) for line in file.read().splitlines()]

seen = [[[float('inf') for _ in range(4)] for c in range(len(maze[0]))] for r in range(len(maze))]

directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def get_neighbours(r, c, grid):
    neighbours = []
    for direction, offset in directions.items():
        dr, dc = offset
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == '#':
            continue
        neighbours.append((nr, nc, direction))

    return neighbours


for r, row in enumerate(maze):
    for c, value in enumerate(row):
        if value == 'S':
            start = (r, c)
        if value == 'E':
            end = (r, c)

from time import time
startt = time()
r, c = start
direction = 1
queue = [(0, r, c, direction, ((r, c),))]
paths = []
best_score = float('inf')

while queue and queue[0][0] <= best_score:
    score, r, c, dir, path = heapq.heappop(queue)

    if (r, c) == end:
        best_score = score
        paths.append(path)
        continue

    if seen[r][c][dir] < score:
        continue
    seen[r][c][dir] = score

    for nr, nc, new_direction in get_neighbours(r, c, maze):
        if (nr, nc) not in path:
            cost = 1 if new_direction == dir else 1001
            heapq.heappush(queue, (score + cost, nr, nc, new_direction, path + ((nr, nc),)))

seats = set()
for path in paths:
    seats |= set(path)
print(len(seats))
print(time() - startt)