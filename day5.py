from functools import cmp_to_key


with open("inputs/day5_input.txt") as file:
    reference, updates = [data.splitlines() for data in file.read().split("\n\n")]

updates = [list(map(int, line.split(','))) for line in updates]
reference =[list(map(int, line.split("|"))) for line in reference]

def cmp(x, y):
    return 1 if y in after_this_num.get(x, []) else -1


def check_after_num(line):
    for i in range(len(line)):
        before =line[:i]
        current = line[i]
        for res in after_this_num.get(current, []):
            if res in before:
                return False
    return True


def return_middle(seq):
    return seq[(len(seq)-1)//2]

before, after = list(map(list, zip(*reference)))
after_this_num = {key: [] for key in set(before)}

for i in range(len(after)):
    after_this_num[before[i]].append(after[i])
 
part1_answer = sum([return_middle(line) for line in updates if check_after_num(line)])
print(part1_answer)

# PART 2
total = 0
incorrect = [line for line in updates if not (check_after_num(line))]
for line in incorrect:
    corrected = (sorted(line, key=cmp_to_key(cmp)))
    total += return_middle(corrected)
    
print(total)
