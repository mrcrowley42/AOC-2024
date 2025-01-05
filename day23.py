from itertools import combinations
from collections import defaultdict
from time import time
start = time()
with open("inputs/day23_input.txt") as file:
    input = file.read().splitlines()

connections = defaultdict(set)

for line in input:
    a, b = line.split("-")
    connections[a].add(b)
    connections[b].add(a)

def is_viable(trio):
    a, b, c = trio
    if not (a in connections[b] and a in connections[c]):
        return False
    if not (b in connections[a] and b in connections[c]):
        return False
    if not (c in connections[a] and a in connections[b]):
        return False
    
    return True

# possible = [trio for trio in combinations(connections.keys(), r=3) if any([x.startswith("t") for x in trio])]
# total = 0
# for trio in possible:
#     if is_viable(trio):
#         total += 1

# print(total)
# print(time() - start)
# print(len(possible))

sets = set()

for x in connections:
    for y in connections[x]:
        for z in connections[y]:
            if x != z and x in connections[z]:
                sets.add(tuple(sorted([x, y, z])))


print(len([s for s in sets if any(cn.startswith("t") for cn in s)]))