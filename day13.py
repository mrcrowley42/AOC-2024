import re 


with open("inputs/day13_input.txt") as file:
    input = [line.splitlines() for line in file.read().split('\n\n')]


def get_tokens(game):
    a, b, prize = [list(map(int,re.findall(r"\d+", line))) for line in game]
    ax, ay = a
    bx, by = b
    px, py = prize
    # px += 10000000000000
    # py += 10000000000000
    a_presses = (px * by - py * bx) / (ax * by - ay * bx)
    b_presses = (px - ax * a_presses) / bx

    if a_presses % 1 == 0 and b_presses % 1 == 0:
        return int((a_presses * 3) + b_presses)
    
    return 0

    # for a_press in range(101):
    #     for b_press in range(101):
    #         new_x = a_press*ax + b_press*bx
    #         new_y = a_press*ay + b_press*by
    #         if new_x > prize[0] and new_y > prize[1]:
    #             break
    #         if [new_x, new_y] == prize:
    #             print(a_press, b_press)
    #             return a_press * 3 + b_press
            
    # return 0


print(sum([get_tokens(game) for game in input]))
