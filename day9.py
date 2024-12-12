with open("inputs/day9_input.txt") as file:
    input = file.read()

files = input[::2]
spaces = input[1::2]

id = 0
result = []
for i in range(len(files)):
    for b in range(int(files[i])):
        result.append(id)
    id += 1
    if i < len(spaces):
        for b in range(int(spaces[i])):
            result.append('.')

blanks = [index for index, value in enumerate(result) if value == '.']

iterations = 0
for i in range(len(result)-1, -1, -1):
    if iterations % 100 == 0:
        print(iterations/len(result)*100)
    iterations += 1
    if '.' not in set(result[:i]):
        break
    if result[i] != '.':
        for blank in blanks: 
            result[blank] = result[i]
            result[i] = '.'
            blanks.pop(0)
            break

checksum = 0
for i in range(len(result)):
    value = result[i]
    if value != '.':
        checksum += (i * value)
print(checksum)








with open("inputs/day9_input.txt") as file:
    input = file.read()

files = input[::2]
spaces = input[1::2]

id = 0
result = []
for i in range(len(files)):
    for b in range(int(files[i])):
        result.append(id)
    id += 1
    if i < len(spaces):
        for b in range(int(spaces[i])):
            result.append('.')

blanks = [index for index, value in enumerate(result) if value == '.']

for index in blanks:
    if len(result) < index:
        break
    while result[-1] == '.':
        result.pop()
    result[index] = result[-1]
    result.pop()

checksum = sum([index * value for index, value in enumerate(result)])
print(checksum)