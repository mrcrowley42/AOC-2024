from time import time


with open("inputs/day6_input.txt") as file:
    input = [list(line) for line in file.read().splitlines()]

direction_map = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

def is_end(location):
    r, c = location
    if (r < 0 or r > len(input[0]) -1) or(c < 0 or c > len(input) -1):
        return True
    return False


def get_start():
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "^":
                return (r, c)


def track_movement(start, input, part2=False):
    direction = 0
    previous = start
    locations = {previous}
    start_t = time()
    threshold = 0
    while True:
        r, c = previous
        dy, dx = direction_map[direction]
        location = (r+dy, c+dx)
        r, c = location
        
        if is_end(location):
            return False if part2 else locations 

        if input[r][c] == "#":
            direction = (direction + 90) % 360 
            continue
        locs = len(locations)
        locations.add((r, c))
        if len(locations) == locs:
            threshold += 1
        
        previous = location

        if threshold > 5000:
            return True
        # if time() - start_t> 2.0:
        #     return "infinite"
        
start = time()
start_pos = get_start()
locations = track_movement(start_pos, input)
# PART 1 ANSWER
print(len(locations))
print(time()-start)

from copy import deepcopy
loops = 0
progress = 0
locations.remove(start_pos)
for location in locations:
    progress += 1
    # print((progress/len(locations)) * 100 ,end="\r")
    new_grid = deepcopy(input)
    r, c = location
    new_grid[r][c] = "#"
    if track_movement(start_pos, new_grid, part2=True):
        loops += 1

print(loops)