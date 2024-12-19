with open("inputs/day19_input.txt") as file:
    avaiable, desired = [group.splitlines() for group in file.read().split('\n\n')]

avaiable = avaiable[0].split(', ')


def check_possible(design:str):
    can_use = [pattern for pattern in avaiable if pattern in design]
    pool = set([item for item in can_use if design.startswith(item)])
    for _ in range(len(design)):
        if design in pool:
            return True
        new_pool = []
        for item in pool:
            new_pool += [item + part for part in can_use if design.startswith((item + part))]
        pool = set(new_pool)

    return False
    
from time import time
start = time()
possible = 0
for design in desired:
    if check_possible(design):
        possible += 1
            
print(possible)
print(time() - start)