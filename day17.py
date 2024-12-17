with open("inputs/day17_input.txt") as file:
    input = file.read().split('\n\n')

steps = list(map(int, input[1].split(':')[1].split(',')))
register = [int(line.split(":")[1]) for line in input[0].splitlines()]
registers = {key: value for key, value in zip(list('ABC'), register)}

def adv(operand):
    registers["A"] = registers["A"] // (2**combo(operand))

def bxl(operand):
    registers["B"] = registers["B"] ^ operand

def bst(operand):
    registers["B"] = combo(operand) % 8

def bxc(operand):
    registers['B'] = registers['B'] ^ registers["C"]

def bdv(operand):
    registers["B"] = registers["A"] // (2**combo(operand))

def cdv(operand):
    registers["C"] = registers["A"] // (2**combo(operand))

def combo(operand):
    if operand < 4:
        return operand
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']

operation = {0: adv, 1: bxl, 2: bst, 4: bxc, 6: bdv, 7: cdv}  

index = 0
output = []
while index < len(steps):
    opcode = steps[index]
    operand = steps[index + 1]
    if opcode == 3:
        if registers["A"] == 0:
            pass
        else:
            index = operand
            continue
    elif opcode == 5:
        value = combo(operand) % 8
        output.append(value)
    else:
        operation[opcode](operand)
    index += 2

print(",".join(list(map(str, output))))

for i in range(1000000000):
    # print(i,end="\r")
    registers = {key: value for key, value in zip(list('ABC'), register)}
    registers["A"] = i
    index = 0
    output = []
    while index < len(steps):
        opcode = steps[index]
        operand = steps[index + 1]
        if opcode == 3:
            if registers["A"] == 0:
                pass
            else:
                index = operand
                continue
        elif opcode == 5:
            value = combo(operand) % 8
            output.append(value)
        else:
            operation[opcode](operand)
        index += 2

    if output == steps:
        print(i)
        exit()
