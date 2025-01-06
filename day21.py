from collections import deque
from time import time
from itertools import product
with open("inputs/day21_input.txt") as file:
    input = file.read().splitlines()

direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
keypad = [list("789"), list("456"), list("321"), list("X0A")]
remote = [list('X^A'), list("<v>")]
keypad_start = (3, 2)

def find_paths(device, start):
    possible = []
    for target_key in input[0]:
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
                        good.append(sequence + key + "A")
                        target_length = len(sequence) + 1
                        start = (nr, nc)
                    continue
                queue.append((nr, nc, sequence + key, path + ((nr, nc),)))
        if possible:
            possible = ["".join(x) for x in product(possible, good)]
        else:
            possible = good

    return(list(possible))

keypad_paths = find_paths(keypad, keypad_start)
print(keypad_paths)

#                     if best_len < len(path) + 1:
#                         break

#                     best_len = len(path) + 1
#                     found_paths.append("".join(presses) + key + "A")
#                     # new_start = (r, c)
#                     continue
#                 else:
#                     queue.append((nr, nc, 

# def find_keypad_paths(device, start, target_code):
#     valid_paths = []
#     for target_key in target_code:
#         r, c = start
#         queue = deque([(r, c, (), ())])
#         best_len = float('inf')
#         found_paths = []
#         new_start = None
#         while queue:
#             r, c, path, presses = queue.popleft()
#             for key, (dr, dc) in direction_map.items():
#                 nr, nc = r + dr, c + dc
#                 if nr < 0 or nc < 0 or nc >= len(device[0]) or nr >= len(device):
#                     continue
#                 if device[nr][nc] == "X":
#                     continue
#                 if (nr, nc) in path:
#                     continue
#                 if device[r][c] == target_key:
#                     if best_len < len(path) + 1:
#                         break

#                     best_len = len(path) + 1
#                     found_paths.append("".join(presses) + key + "A")
#                     # new_start = (r, c)
#                     continue
#                 else:
#                     queue.append((nr, nc, path + ((nr, nc),), presses + (key,)))

#         continued_path = []
#         if valid_paths:
#             for existing in valid_paths:
#                 for pathway in found_paths:
#                     continued_path.append(existing + pathway)
#         else:
#             continued_path = found_paths
#         valid_paths = continued_path

#         # start = new_start
#         print(valid_paths)
#     return set(valid_paths)


# start_t = time()
# total = 0

# for line in input:
#     paths = (find_keypad_paths(keypad, (3, 2), line))
    # print(paths)
    # print(len(paths))
    # best_length = float('inf')
    # paths = [find_keypad_paths(remote, (0, 2), path) for path in paths]
#     next_paths = []
#     for x in paths:
#         for y in x:
#             if len(y) <=  best_length:
#                 best_length = len(y)
#                 next_paths.append(y)

#     best_length = float('inf')
#     paths = [find_keypad_paths(remote, (0, 2), path) for path in next_paths]
#     next_paths = []
#     for x in paths:
#         for y in x:
#             if len(y) <=  best_length:
#                 best_length = len(y)
#                 next_paths.append(y)


#     print(next_paths)

#     total += best_length * int("".join([char for char in line if char.isdigit()]))

# print(total)
# print(time() - start_t)
# for path in next_paths:
#     print(len(path))

# def path_to_key(start, target, device):
#     r, c = start
#     queue = deque([(r, c, 0, ())])
#     while queue:
#         r, c, score, path = queue.popleft()

#         if device[r][c] == target:
#             return "".join(path) + "A", (r, c)

#         for key, (dr, dc) in direction_map.items():
#             nr, nc = r + dr, c + dc
#             if nr < 0 or nc < 0 or nc >= len(device[0]) or nr >= len(device):
#                 continue
#             if device[nr][nc] == "X":
#                 continue

#             queue.append((nr, nc, score + 1, path + ((key),) ))

# start = (3, 2)


# def path_for_sequence(target, start, device):
#     full_path = ""
#     for key in target:
#         path, start = path_to_key(start, key, device)
#         full_path += path

#     return full_path


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
