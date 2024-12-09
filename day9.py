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
# print("".join(list(map(str, result))))

# def sort_memory():


iterations = 0
for i in range(len(result)-1, -1, -1):
    if iterations % 100 == 0:
        print(iterations/len(result)*100)
    iterations += 1
    if '.' not in set(result[:i]):
        break
    if result[i] != '.':
        for j in range(len(result)):
            if result[j] == '.':
                result[j] = result[i]
                result[i] = '.'


                
    # print("".join(list(map(str, result))))



# print(result)
checksum = 0
for i in range(len(result)):
    value = result[i]
    if value != '.':
        # print(value*i)
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