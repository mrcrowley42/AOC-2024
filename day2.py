with open("inputs/day2_input.txt") as file:
    input = file.read().splitlines()

    
numbers = [list(map(int, line.split())) for line in input]

def fast():
    count = 0
    for x_line in numbers:
        for i in range(len(x_line)):
            line = x_line[:i]+x_line[i+1:]
            if line == sorted(line) or line == sorted(line, reverse=True):
                if all([ 0 < (abs(line[i] - line[i-1])) < 4 for i in range(1, len(line))]):
                    count += 1
                    break
    return count
                
        
        
    

def ascending(line):
    for i in range(1, len(line)):
        if line[i] <= line[i-1]:
            return False
    return True


def descending(line):
    for i in range(1, len(line)):
        if line[i] >= line[i-1]:
            return False
    return True


def is_safe(line):
    if not ascending(line) and not descending(line):
        return 0
    
    for i in range(1, len(line)):
        if not 0 < (abs(line[i] - line[i-1])) < 4:
            return 0
    return 1
   
            
def any_safe(line):
    for i in range(len(line)):
        new_line = line[:i]+line[i+1:]
        if is_safe(new_line):
            return 1
    return 0


print((sum([any_safe(line) for line in numbers])))
print(fast())