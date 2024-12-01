from collections import Counter

with open("inputs/day1_input.txt") as file:
    input = file.read().splitlines()

numbers = [list(map(int, line.split())) for line in input]
left = sorted([line[0] for line in numbers])
right = sorted([line[1] for line in numbers])
diffs = [abs(left[i] - right[i]) for i in range(len(numbers))]
# Part 1
print(sum(diffs))

counts = Counter(right)
sim_scores = [id * count for id, count in counts.items() if id in left]
# Part 2 
print(sum(sim_scores))