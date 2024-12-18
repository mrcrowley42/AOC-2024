from collections import deque

with open("inputs/day18_input.txt") as file:
    input = [list(map(int, line.split(","))) for line in file.read().splitlines()]


direction_map = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

def get_neighbours(grid, r, c):
    neighbours = []
    for offset in direction_map.values():
        dy, dx = offset
        r2, c2 = r + dy, c + dx
        if not (0 <= r2 < grid_length and 0 <= c2 < grid_length):
            continue
        if grid[r2][c2] == '#':
            continue
        neighbours.append((r2, c2,))
    return neighbours

grid_length = 71
grid = [['.' for c in range(grid_length)] for r in range(grid_length)]
n_bytes = 1024
for i in range(n_bytes):
    c, r = input[i]
    grid[r][c] = "#"

visited = {(0, 0)}
queue = deque([(0, 0, 0)])

while queue:
    steps, r, c = queue.popleft()
    if (r, c) == (grid_length-1, grid_length-1):
        print(steps)
        break
    for nr, nc in get_neighbours(grid, r, c):
        if (nr, nc) in visited:
            continue
        queue.append((steps + 1, nr, nc))
        visited.add((nr, nc))



# from time import time
# t = time()
# grid_length = 71
# grid = [['.' for c in range(grid_length)] for r in range(grid_length)]
# n_bytes = 1024

# for i in range(n_bytes):
#     c, r = input[i]
#     grid[r][c] = "#"

# for i in range(1024, len(input)):
#     # print(i)
#     col, row = input[i]
#     grid[row][col] = "#"
#     visited = {(0, 0)}
#     queue = deque([(0, 0, 0)])
#     found = False
#     while queue:
#         steps, r, c = queue.popleft()
#         if (r, c) == (grid_length-1, grid_length-1):
#             found = True
#             break
#         for nr, nc in get_neighbours(grid, r, c):
#             if (nr, nc) in visited:
#                 continue
#             queue.append((steps + 1, nr, nc))
#             visited.add((nr, nc))

#     if not found:
#         print(f"{i} | ({col, row})")
#         break

# print(time() -t)



def path_exists(grid):
    visited = {(0, 0)}
    queue = deque([(0, 0, 0)])
    while queue:
        steps, r, c = queue.popleft()
        if (r, c) == (grid_length-1, grid_length-1):
            return True
        for nr, nc in get_neighbours(grid, r, c):
            if (nr, nc) in visited:
                continue
            queue.append((steps + 1, nr, nc))
            visited.add((nr, nc))

    return False

low, high = 1024, len(input)

while low < high:
    grid2 = [['.' for c in range(grid_length)] for r in range(grid_length)]
    mid = (low + high) // 2
    for i in range(mid+1):
        col, row = input[i]
        grid2[row][col] = "#"
    
    if path_exists(grid2):
        low = mid + 1
    else:
        high = mid

print(low)
