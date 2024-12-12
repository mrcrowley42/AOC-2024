with open("inputs/day4_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]

offsets = [-1, 0, 1]

def find_neighbours(row, column, grid):
    if grid[column][row] != "A":
        return False
    neighbours = []
    correct = ["ms", "sm"]
    offset_x = [-1, 1, -1, 1]
    offset_y = [-1, 1, 1, -1]
    rows = len(grid)
    columns = len(grid[0])
    for i in range(len(offset_x)):
        x_pos = row + offset_x[i]
        y_pos = column + offset_y[i]
        if (x_pos < 0 or x_pos >= columns) or (y_pos < 0 or y_pos >= rows):
            continue
        neighbours.append(grid[y_pos][x_pos])
        
    return "".join(neighbours[:2]).lower() in correct and "".join(neighbours[2:]).lower() in correct


def find_word(r, c, input):
    if input[r][c] != "X":
        return 0
    count = 0
    for dr in offsets:
        for dc in offsets:
            if dr == dc == 0:
                continue
            sub_str = "X"
            for i in range(1,4):
                new_r = r + (dr * i)
                new_c = c + (dc * i)
                if (0 > new_r or new_r > len(input)-1) or ( 0 > new_c or new_c > len(input[0])-1):
                    continue 

                sub_str += input[new_r][new_c]
            if sub_str == "XMAS":
                count += 1
                
    return count
        

count = sum(find_word(i, j, input) for i in range(len(input)) for j in range(len(input[0])))
print(count)

xmas_count = sum(find_neighbours(i, j, input) for i in range(len(input)) for j in range(len(input[0])))   
print(xmas_count)
