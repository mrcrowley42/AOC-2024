with open("inputs/day2_input.txt") as file:
    input = file.read().splitlines()

    
numbers = [list(map(int, line.split())) for line in input]

def ascending(line):
    return all(line[i] > line[i-1] for i in range(1, len(line)))


def descending(line):
    return all(line[i] < line[i-1] for i in range(1, len(line)))


def is_safe(line):
    if not (ascending(line) or descending(line)):
        return 0
    return 1 if all(0 < (abs(line[i] - line[i-1])) < 4 for i in range(1, len(line))) else 0


def any_safe(line):
    return 1 if any(is_safe(line[:i]+line[i+1:]) for i in range(len(line))) else 0


print((sum(is_safe(line) for line in numbers)))
print((sum(any_safe(line) for line in numbers)))
