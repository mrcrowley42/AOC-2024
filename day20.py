from collections import deque, Counter


with open("inputs/day20_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]

for r, row in enumerate(input):
    for c, value in enumerate(row):
        if value == 'S':
            start = (r, c)
        if value == 'E':
            end = (r, c)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def control_steps(start, grid):
    r, c = start
    score_map = dict()
    vistied = {(r, c)}
    queue = deque([(r, c, 0,)])
    score_map[(r,c)] = 0
    while queue:
        r, c, score = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in vistied:
                continue
            if grid[nr][nc] == "#":
                continue
            vistied.add((r, c))
            score_map[(nr, nc)] = score + 1
            queue.append((nr, nc, score + 1))

    return score_map

score_map = control_steps(start, input)

# print(score_map[end])

count = 0
scores = []
for r, row in enumerate(input):
    for c, value in enumerate(row):
        if value == "#":
            continue
        for radius in range(2, 21):
            for dr in range(radius +1):
                dc = radius - dr
                for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                    if nr < 0 or nc < 0 or nc >= len(row) or nr >= len(input):
                        continue
                    if input[nr][nc] == "#":
                        continue
                    diff = score_map[(r, c)] - score_map[(nr, nc)] - radius
                    if diff >= 100:
                        scores.append(diff)
                        count += 1

print(count)
# print(Counter(scores))
