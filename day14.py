import re
from math import prod

class Robot:
    def __init__(self, data):
        self.x, self.y, self.dir_x, self.dir_y = list(map(int, data))
        self.new_x, self.new_y = 0, 0

    def move(self, seconds=1):
        self.new_x = (self.x + self.dir_x * seconds) % WIDTH
        self.new_y = (self.y + self.dir_y * seconds) % HEIGHT
    
    def grid_location(self):
        return self.new_y, self.new_x
    

def return_quad(location):
    y, x = location
    if x < half_x and y < half_y:
        return 'top_left'
    if x > half_x and y < half_y:
        return 'top_right'
    if x < half_x and y > half_y:
        return 'bottom_left'
    if x > half_x and y > half_y:
        return 'bottom_right'
    return None


def print_tree(seconds):
    grid = [[0 for c in range(WIDTH)] for r in range(HEIGHT)]
    for robot in robots:
        robot.move(seconds)
        r, c = robot.grid_location()
        grid[r][c] += 1
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value < 1:
                grid[r][c] = " "
            else:
                grid[r][c] = "#"

    [print("".join(list(map(str, line)))) for line in grid]


def return_answer(part1=True):
    factor = (len(robots)/4)**4
    seconds = None
    max_seconds = 2 if part1 else WIDTH * HEIGHT

    for i in range(1, max_seconds):
        quads = dict(top_left=0, top_right=0, bottom_left=0, bottom_right=0)
        for robot in robots:
            robot.move(i)
            quad = return_quad(robot.grid_location())
            if quad:
                quads[quad] += 1

        product = prod(quads.values())
        if product < factor:
            factor = product
            seconds = i
            
    return product if part1 else seconds


with open("inputs/day14_input.txt") as file:
    input = file.read().splitlines()

WIDTH, HEIGHT = 101, 103
robots = [Robot(re.findall(r"-?\d+", line)) for line in input]
half_x, half_y = (WIDTH-1)//2,  (HEIGHT-1)//2

print(return_answer())
tree_seconds = return_answer(part1=False)
print(tree_seconds)
# print_tree(tree_seconds)
