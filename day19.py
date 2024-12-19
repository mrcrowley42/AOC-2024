from itertools import product as n_combinations
from time import time


start = time()


with open("inputs/day19_input.txt") as file:
    avaiable, desired = [group.splitlines() for group in file.read().split('\n\n')]

avaiable = avaiable[0].split(', ')

# for design in desired:
#     can_use = [pattern for pattern in avaiable if pattern in design]
#     print(len(can_use))
#     possible = 
#     if design in possible:


possible = 0
wanted = set(desired)

# for i in range(1, len(avaiable)):
#     # print(i)
#     if len(wanted) < 1:
#         break
#     combinations = ["".join(comb) for comb in list(n_combinations(avaiable, repeat=i))]
#     remove = []
#     for design in wanted:
#         if design in combinations:
#             possible += 1
#             # print(design)
#             remove.append(design)
            
#     for item in remove:
#         wanted.remove(item)

def check_possible(design):
    can_use = [pattern for pattern in avaiable if pattern in design]
    for i in range(1, len(design)+1):
        combinations = (n_combinations(can_use, repeat=i))
        for combination in combinations:
            # if design[0] != combination[0]:
            #     continue
            if design == "".join(combination):
                return True
    print(design)
    return False
    
for design in desired:
    if check_possible(design):
        possible += 1
            
print(possible)
print(time() - start)