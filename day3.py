import re
from math import prod
with open("inputs/day3_input.txt") as file:
    input = file.read()

p1_total = 0
p2_total = 0
enabled = True
matches = re.findall(r"mul\(\d*,\d*\)|do\(\)|don\'t\(\)", input)

for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        nums = re.findall(r"\d+", match)
        if enabled:
            p2_total += prod(list(map(int,nums)))
        p1_total += prod(list(map(int,nums)))
        
print(p1_total)
print(p2_total)
