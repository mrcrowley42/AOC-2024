import numpy


with open("inputs/day4_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]


np_array = numpy.matrix(input)
np_flip = numpy.fliplr(np_array)
diagonals = []

for array in [np_array, np_flip]:
    for i in range(-(len(input)), len(input)):
        diagonals.append("".join(array.diagonal(i).tolist()[0]))

rows = ["".join(line) for line in input]
columns = ["".join([line[i] for line in input ]) for i in range(len(input[0]))]

num = 0

for lines in [rows, columns, diagonals]:
    for line in lines:
        num += len(line.split("XMAS")) -1
        num += len(line[::-1].split("XMAS")) -1

print(num)


def find_neighbours(row, column, grid):
    if grid[column][row] != "A":
        return False
    neighbours = []
    correct = ["ms", "sm"]
    offset_x = [-1, 1, -1, 1]
    offset_y = [-1,  1, 1, -1]
    rows = len(grid)
    for i in range(len(offset_x)):
        columns = len(grid[0])
        x_pos = row + offset_x[i]
        y_pos = column + offset_y[i]
        if (x_pos < 0 or x_pos >= columns or y_pos < 0 or y_pos >= rows):
            continue
        neighbours.append(grid[y_pos][x_pos])
        
    return "".join(neighbours[:2]).lower() in correct and "".join(neighbours[2:]).lower() in correct


xmas_count = 0
for i in range(len(input[0])):
    for j in range(len(input)):
       if (find_neighbours(i, j, input)):
           xmas_count += 1
           
print(xmas_count)