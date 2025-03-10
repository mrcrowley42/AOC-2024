from copy import deepcopy


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

# PART 1
blanks = [index for index, value in enumerate(result) if value == '.']

results = deepcopy(result)

for i in range(len(results)-1, -1, -1):
    if results[i] != '.':
        blank = blanks.pop(0)
        if i < blank:
            break
        results[blank] = results[i]
    results.pop(i)
       
checksum = sum([index * value for index, value in enumerate(results)])
print(checksum)

# PART 2 
blanks = []
space = []
files = []
file = []
current_id = 100
for index, value in enumerate(result):
    if value == '.':
        space.append(index)
        if file:
            files.append(dict(start=file[0], length=len(file), id = current_id))
            file = []
    elif value == current_id:
        file.append(index)
    else:
        if file:
            files.append(dict(start=file[0], length=len(file), id = current_id))
            file = []
        file.append(index)
        current_id = value
        if space:
           blanks.append(dict(start=space[0], length=len(space)))
           space = []
if space:
    blanks.append([space[0], len(space)])

if file:
    files.append(dict(start=file[0], length=len(file), id = result[file[0]]))

files = files[::-1]
# print("".join(map(str,result)))

for file in files:
    for index, blank in enumerate(blanks):
        # print(index)
        if file['length'] <= blank['length']:
            if file['start'] >= blank['start']:
                
                for i in range(blank['start'], blank['start'] + file['length']):
                    result[i] = file['id']

                for i in range(file['start'], file['start'] + file['length']):
                    result[i] = '.'
                blank['length'] -= file['length']
                blank['start'] += file['length']
                if blank['length'] <= 0:
                    blanks.pop(index)
                break
        # print("".join(map(str,result)))

# print("".join(map(str,result)))


checksum = sum([index * value for index, value in enumerate(result) if value != '.'])
print(checksum)


# ALTERNATE PART 1

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