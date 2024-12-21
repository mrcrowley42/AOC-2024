with open("inputs/day21_input.txt") as file:
    input = file.read().splitlines()

direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

keypad = [[7, 8, 9],
          [4, 5, 6],
          [3, 2, 1],
          ['X', 0, 'A']]

remote = [['x', '^', 'A'],
          ['<', 'v', '>']]

#what