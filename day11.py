from copy import deepcopy


with open("inputs/day11_input.txt") as file:
    input = list(map(int, file.read().split()))


def blink(rock):
    if rock == 0:
        return [1]
    
    rock_str = str(rock)
    if len(rock_str) % 2 == 0:
        index = len(rock_str) // 2
        return [int(rock_str[:index]), int(rock_str[index:])]
    
    return [rock * 2024]


def stone_count(blinks):
    rocks = deepcopy(input)
    rock_dict = {rock: rocks.count(rock) for rock in rocks}

    for n in range(blinks):
        results = dict()
        for rock, count in rock_dict.items():
            for result in blink(rock):
                results[result] = results.get(result, 0) + count

        rock_dict = results

    return(sum(x for x in rock_dict.values()))    


# Naive method
rocks = deepcopy(input)
for i in range(25):
    rocks = [val for rock in rocks for val in blink(rock)]
# PART 1
print(len(rocks))
# PART 2
print(stone_count(75))
