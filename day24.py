import operator

with open("inputs/day24_input.txt") as file:
    initial, connections = file.read().split("\n\n")


wires = dict()

for line in initial.splitlines():
    name, value = line.split(': ')
    wires[name] = int(value)

ops = {"AND": operator.and_, "XOR": operator.xor, "OR": operator.or_ }

to_do = []

for line in connections.splitlines():
    a, op, b, empty, output = line.split()
    to_do.append([a, op, b, output])

while to_do:
    for item in to_do:
        a, op, b, output = to_do.pop()
        try:
            wires[output] = ops[op](wires[a], wires[b])
            
        except KeyError:
            to_do.insert(0, [a, op, b, output])
            continue
        

# print(wires)

to_parse = sorted([(x, y)  for x, y in wires.items() if x.startswith('z')], key=lambda x: x[0], reverse=True)

bin_string = ""

for key, digit in to_parse:
    bin_string += str(digit)

# print(bin_string)

print(int(bin_string, base=2))