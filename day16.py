# import heapq 
from collections import deque


with open("inputs/day16_input.txt") as file:
    maze = [list(line) for line in file.read().splitlines()]

direction_map = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

def get_neighbours(r, c):
    neighbours = []
    for deg, offset in direction_map.items():
        dy, dx = offset
        r2, c2 = r + dy, c + dx
        if maze[r2][c2] != '#':
            neighbours.append((r2, c2))
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
visited = {start}
queue = deque([(0 ,r, c)])

while queue:
    score, r, c = queue.popleft()
    if (r, c) == end:
        print(score)
        break
    for location in get_neighbours(r, c):
        if location in visited:
            continue
        nr, nc = location
        queue.append((score + 1, nr, nc))
        visited.add((nr, nc))

# direction = 90
# r, c = start
# visited = {(r, c, direction)}
# pq = [(0, r, c, direction)]
# while pq:
#     cost, r, c, direction = heapq.heappop(pq)

# print(search(start, end, maze))
