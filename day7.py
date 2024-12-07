from itertools import product
import operator


with open("inputs/day7_input.txt") as file:
    input = [line.split(":") for line in file.read().splitlines()]


def concat(a, b):
    return int(str(a) + str(b))


operation = {'*': operator.mul, '+': operator.add, '|': concat}


def check_line(line):
    global done
    result, nums = line
    required_result = int(result)
    nums = list(map(int,nums.split()))
    combinations = list(product(list("+*|"), repeat=len(nums)-1))
    for operators in combinations:
        joined = []
        for i in range(len(nums)):
            if i < len(operators):
                joined.append([nums[i], operators[i]])
            else:
                joined.append([nums[i]])
        
        result = 0
        for j in range(len(joined)-1):
            if j == 0:
                result = operation[joined[j][1]](joined[j][0], joined[j+1][0])
            else:
                result = operation[joined[j][1]](result, joined[j+1][0])

        if result == required_result:
            done += 1
            if done % 10 == 0:
                print((done /len(input)) *100, end="\r")
            return required_result
        
    done += 1

    if done % 10 == 0:
                print((done /len(input)) *100, end="\r")
    return 0
done = 0
results = [check_line(line) for line in input]
print("\n")
print(sum(results))
