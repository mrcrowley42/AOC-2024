from collections import deque


with open("inputs/day21_input.txt") as file:
    input = file.read().splitlines()

direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
keypad = [list("789"), list("456"), list("321"), list("X0A")]
remote = [list('X^A'), list("<v>")]

def path_to_key(start, target, device):
    r, c = start
    queue = deque([(r, c, 0, ())])
    while queue:
        r, c, score, path = queue.popleft()

        if device[r][c] == target:
            return "".join(path) + "A", (r, c)
        
        for key, (dr, dc) in direction_map.items():
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nc >= len(device[0]) or nr >= len(device):
                continue
            if keypad[nr][nc] == "X":
                continue
            queue.append((nr, nc, score + 1, path + ((key),) ))


def path_for_sequence(targets, start, device):
    full_path = ""
    for target in targets:
        path, start = path_to_key(start, target, device)
        full_path += path

    return full_path

targets = list(input[0])
start = (3, 2)
required_buttons = path_for_sequence(targets, start, keypad)

print(required_buttons)


pad_start = (0, 2)


