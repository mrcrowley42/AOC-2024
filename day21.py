from collections import deque
from time import time
from itertools import product
from functools import cache
with open("inputs/day21_input.txt") as file:
    input = file.read().splitlines()

direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
keypad = [list("789"), list("456"), list("123"), list("X0A")]
remote = [list('X^A'), list("<v>")]
keypad_start = (3, 2)
remote_start = (0, 2)


def find_paths(target_keys, device, start):
    possible = []
    for target_key in target_keys:
        sr, sc = start
        queue = deque([(sr, sc, "", (sr, sc))])
        good = []
        target_length = float("inf")
        while queue:
            r, c, sequence, path = queue.popleft()
            for key, (dr, dc) in direction_map.items():
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nc >= len(device[0]) or nr >= len(device):
                    continue
                if device[nr][nc] == "X":
                    continue
                if (nr, nc) in path:
                    continue
                if device[nr][nc] == target_key:
                    if len(sequence) + 1 <= target_length:
                        start = (nr, nc)
                        good.append(sequence + key + "A")
                        target_length = len(sequence) + 1

                    continue
                queue.append((nr, nc, sequence + key, path + ((nr, nc),)))
        if possible:
            possible = ["".join(x) for x in product(possible, good)]
        else:
            possible = good

    return tuple(possible)


key_pad_map = dict()

for r, row in enumerate(keypad):
    for c, value in enumerate(row):
        for destination in list("0123456789A"):
            if value == destination:
                key_pad_map[(value, destination)] = ['A']
            else:
                key_pad_map[(value, destination)] = find_paths(
                    destination, keypad, (r, c))

dir_pad_map = dict()

for r, row in enumerate(remote):
    for c, value in enumerate(row):
        for destination in list("<>v^A"):
            if value == destination:
                dir_pad_map[(value, destination)] = ['A']
            else:
                dir_pad_map[(value, destination)] = find_paths(
                    destination, remote, (r, c))


def faster_solve(device_map, code):
    start = "A"
    paths = []
    for key in code:
        paths.append(device_map[start, key])
        start = key

    return ["".join(x) for x in list(product(*paths))]


def find_complexity(code):
    sequence = faster_solve(key_pad_map, code)
    for _ in range(2):
        possible_next = []
        for seq in sequence:
            possible_next += faster_solve(dir_pad_map, seq)

        min_len = min(map(len, possible_next))
        sequence = [seq for seq in possible_next if len(seq) == min_len]

    numeric_part = int("".join([char for char in code if char.isdigit()]))
    return len(sequence[0]) * numeric_part


print(sum([find_complexity(target) for target in input]))
