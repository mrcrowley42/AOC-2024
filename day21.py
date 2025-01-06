from collections import deque


with open("inputs/day21_input.txt") as file:
    input = file.read().splitlines()

direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
keypad = [list("789"), list("456"), list("321"), list("X0A")]
remote = [list('X^A'), list("<v>")]

def path_to_key(start, target, device):
    r, c = start
    queue = deque([(r, c, 0, ())])
    visited = set()
    paths = []
    fr = fc = None
    while queue:
        r, c, score, path = queue.popleft()

        if device[r][c] == target:
            paths.append(("".join(path) + "A"))
            fr, fc = r, c
            continue
        
        for key, (dr, dc) in direction_map.items():
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nc >= len(device[0]) or nr >= len(device):
                continue
            if keypad[nr][nc] == "X":
                continue
            if (nr, nc) in visited:
                continue
            queue.append((nr, nc, score + 1, path + ((key),) ))
            visited.add((nr, nc))

    return paths, (fr, fc)

start = (3, 2)


def path_for_sequence(target, start, device):
    full_paths = set()
    for key in target:
        new_paths = set()
        paths, start = path_to_key(start, target, device)
        for path in paths:
            for existing in full_paths:
                new_paths.add(existing + path)
                
        full_paths = new_paths


    return full_paths

path_for_sequence(input[0], start, keypad)

# def find_complexity(target):
#     start = (3, 2)
#     pad_start = (0, 2)
#     required_buttons = path_for_sequence(target, start, keypad)
#     required_buttons = path_for_sequence(required_buttons, pad_start, remote)
#     required_buttons = path_for_sequence(required_buttons, pad_start, remote)

#     numeric_part = int("".join([char for char in target if char.isdigit()]))
#     print(len(required_buttons), numeric_part)
#     return len(required_buttons) * numeric_part

# print(sum([find_complexity(target) for target in input]))