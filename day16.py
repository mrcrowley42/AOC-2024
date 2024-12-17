import heapq 

with open("inputs/day16_input.txt") as file:
    maze = [list(line) for line in file.read().splitlines()]

direction_map = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

def get_neighbours(r, c, direction):
    neighbours = []
    for deg, offset in direction_map.items():
        dy, dx = offset
        r2, c2 = r + dy, c + dx
        if maze[r2][c2] != '#':
            neighbours.append(((r2, c2), deg))
    return neighbours

for r, row in enumerate(maze):
    for c, value in enumerate(row):
        if value == 'S':
            start = (r, c)
        if value == 'E':
            end = (r, c)


# def search(start, end, maze):
direction = 90
r, c = start
visited = {(r, c, direction)}
pq = [(0, r, c, direction)]
while pq:
    cost, r, c, direction = heapq.heappop(pq)

# print(search(start, end, maze))
