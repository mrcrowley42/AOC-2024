for i in range(17,20):
    with open(f"inputs/day{i}_input.txt", "x") as fi:
        pass
    with open(f"day{i}.py", "x") as fi:
        fi.write(f"""with open("inputs/day{i}_input.txt") as file:
    input = file.read().splitlines()""")

        