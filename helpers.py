class Vector2:
    def __init__(self,r,c):
        self.r, self.c = r, c
        
    def __add__(self, other):
        return Vector2(self.r + other.r, self.c + other.c)
    
    def location(self):
        return (self.r, self.c)   

directions = {"L": Vector2(0, -1), "R": Vector2(0, 1), "D": Vector2(-1, 0), "U": Vector2(1, 0)}

def rows_to_columns(rows):
    return list(map(list, zip(*rows)))

direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


# with open("19-10.txt") as file:
input = [list(line) for line in file.read().splitlines()]

[print("".join(line)) for line in input]

with open("21-9.txt") as file:
    input = [list(map(int, list(line))) for line in file.read().splitlines()]

[print("".join(list(map(str, line)))) for line in input]


with open("22-17.txt") as file:
    input = [list(line) for line in file.read().splitlines()]

[print("".join(line)) for line in input]


# with open("20-25.txt") as file:
#     ranges = re.findall(r'-?\d+', file.read())
from collections import deque


def bfs(start, grid):
    queue = deque([start])
    visited = {start}
    while queue:
        position = queue.popleft()
        r, c = position
        for dr, dc in direction_map.values():
            nr = r + dr
            nc = c + dc
            if (nr, nc) in visited:
                continue
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue
            queue.append((nr, nc))
            visited.add((nr, nc))

