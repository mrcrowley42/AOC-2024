from itertools import combinations
from copy import deepcopy


with open("inputs/day8_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]


def distance_between(p1, p2, iter):
    dx, dy = [p2[0] - p1[0], p2[1] - p1[1]]
    dx *= iter
    dy *= iter
    diff = [p1[0] - dx, p1[1] -dy], [p2[0] + dx, p2[1] + dy]
    answer = [[r, c] for r, c in diff if (r >= 0 and r < len(input)) and (c >= 0 and c < len(input[0]))]
    return answer


def count_result(grid, part1=False):
    count = 0
    for row in grid:
        for column in row:
            if part1:
                if column == "#":
                    count += 1
            else:
                if column != ".":
                    count += 1
                
    return count


def find_signals(part1=False):
    fix = []
    for positions in signal_map.values():
        places = list(combinations(positions, 2))
        for pair in places:
            iter = 1
            while True:
                left, right = pair
                answer = distance_between(left, right, iter)
                for entry in answer:
                    fix.append(entry)
                if part1:
                    break
                iter += 1
                if len(answer) < 1:
                    break
    return fix


signal_map = dict()

for r, row in enumerate(input):
    for c, char in enumerate(row):
        if char != ".":
            signal_map[char] = signal_map.get(char, [])
            signal_map[char].append([r, c])


grid = deepcopy(input)
for r,c in find_signals(part1=True):
    grid[r][c] = "#"

print(count_result(grid, part1=True))

grid = deepcopy(input)
for r,c in find_signals():
    grid[r][c] = "#"
    
print(count_result(grid))