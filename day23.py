from itertools import combinations


with open("inputs/day23_input.txt") as file:
    input = file.read().splitlines()

connections = dict()

for line in input:
    a, b = line.split("-")
    connections[a] = connections.get(a, []) + [b]
    connections[b] = connections.get(b, []) + [a]

def is_viable(trio):
    a, b, c = trio
    if not (a in connections[b] and a in connections[c]):
        return False
    if not (b in connections[a] and b in connections[c]):
        return False
    if not (c in connections[a] and a in connections[b]):
        return False
    
    return True

possible = (trio for trio in combinations(connections.keys(), r=3) if any([x.startswith("t") for x in trio]))
total = 0
for trio in possible:
    if is_viable(trio):
        total += 1

print(total)
