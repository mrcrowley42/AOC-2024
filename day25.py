with open("inputs/day25_input.txt") as file:
    input = [[list(line) for line in group.splitlines()] for group in file.read().split('\n\n')]

locks = []
keys = []
for group in input:
    if set(group[0]) == {'#'}:
        cols = [col.count("#") for col in  list(zip(*group[1:-1]))]
        locks.append(cols)
    if set(group[-1]) == {"#"}:
        cols = [col.count("#") for col in  list(zip(*group[1:-1]))]
        keys.append(cols)
 
total = 0
for key in keys:
    for lock in locks:
        if all([sum(g) < 6 for g in  list(zip(key, lock))]):
            total += 1

print(total)
        