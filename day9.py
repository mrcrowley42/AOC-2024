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

for i in range(len(result)-1, -1, -1):
    if result[i] != '.':
        blank = blanks.pop(0)
        if i < blank:
            break
        result[blank] = result[i]
    result.pop(i)
       
checksum = sum([index * value for index, value in enumerate(result)])
print(checksum)











# with open("inputs/day9_input.txt") as file:
#     input = file.read()

# files = input[::2]
# spaces = input[1::2]

# id = 0
# result = []
# for i in range(len(files)):
#     for b in range(int(files[i])):
#         result.append(id)
#     id += 1
#     if i < len(spaces):
#         for b in range(int(spaces[i])):
#             result.append('.')

# blanks = [index for index, value in enumerate(result) if value == '.']
# for index in blanks:
#     if len(result) < index:
#         break
#     while result[-1] == '.':
#         result.pop()
#     result[index] = result[-1]
#     result.pop()

# checksum = sum([index * value for index, value in enumerate(result)])
# print(checksum)