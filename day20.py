from collections import deque, Counter, OrderedDict

with open("inputs/day20_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]

direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def control_steps(start, grid):
    r , c = start
    score_map = OrderedDict()
    vistied = {(r, c)}
    queue = deque([(r, c, 0,)])
    score_map[(r,c)] = 0
    while queue:
        r, c, score = queue.popleft()
        vistied.add((r, c))
        for dr, dc in direction_map.values():
            nr, nc = r + dr, c + dc
            if (nr, nc) in vistied:
                continue
            if grid[nr][nc] == "#":
                continue
            score_map[(nr, nc)] = score + 1
            queue.append((nr, nc, score + 1))

    return score, score_map


# def should_skip(r, c, grid):
#     around = 0
#     for dr, dc in direction_map.values():
#         nr, nc = r + dr, c + dc
#         if grid[nr][nc] == "#":
#             around += 1
#     return around > 3

for r, row in enumerate(input):
    for c, value in enumerate(row):
        if value == 'S':
            start = (r, c)
        if value == 'E':
            end = (r, c)

control, score_map = control_steps(start, input)


cheats = dict()
checked = 0
threshold = 0
from time import time

print(score_map)

spots = []

# def find_place(r, c):
#     for dr, dc in direction_map.values():
#         nr, nc = r + dr, c + dc
#         if (nr, nc) in score_map.keys():
#             return (nr, nc)
        # if grid[nr][nc] == "#":

# for r_index in range(1, len(input) -1):
#     for c_index in range(1, len(input[0]) -1):
#         # checked += 1
#         # if checked > 1000:
#         #     continue
#         if input[r_index][c_index] != "#":
#             continue
#         if should_skip(r_index, c_index, input):
#             continue
#         # nr, nc = find_place(r_index, c_index)
#         spots.append((r_index, c_index))

# print(len(spots))


def search(cheat):
    r_index, c_index= cheat
    grid = [list(row) for row in input]
    grid[r_index][c_index] = "." 
    vistied = {(sr, sc)}
    queue = deque([(sr,sc, score_map[(sr,sc)])])
    while queue:
        r, c, score = queue.popleft()
        if score > control and cheat in vistied:
            break
        vistied.add((r, c))
        for dr, dc in direction_map.values():
            nr, nc = r + dr, c + dc
            if (nr, nc) in vistied:
                continue
            if grid[nr][nc] == "#":
                continue
            queue.append((nr, nc, score + 1))
    xx = control - score
    if xx > threshold:
        scores[xx] = scores.get(xx, 0) + 1


sr, sc = start
startt = time()
scores = dict()
e = 0
for cheat in spots:
    e += 1
    search(cheat)
    print(e)
   

# blah = OrderedDict(sorted(Counter(scores).items()))
# print(blah)
print(scores)
print(time() - startt)
