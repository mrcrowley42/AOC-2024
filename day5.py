with open("inputs/day5_input.txt") as file:
    reference, updates = [data.splitlines() for data in file.read().split("\n\n")]

updates = [list(map(int, line.split(','))) for line in updates]
reference =[list(map(int, line.split("|"))) for line in reference]


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
before_this_num = {key: [] for key in set(after)}

for i in range(len(after)):
    after_this_num[before[i]].append(after[i])
    before_this_num[after[i]].append(before[i])

part1_answer = sum([return_middle(line) for line in updates if check_after_num(line)])
print(part1_answer)

# PART 2

incorrect = [line for line in updates if not (check_after_num(line))]
print(incorrect)
