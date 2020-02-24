def visualize_board(size, grid):
    for row in range(len(grid)):
        if row != 0:
            string = "- " * (2 * size - 1)
            print("\n" + string)
        else:
            print("")
        for col in range(len(grid)):
            if col != 0:
                print("|", end=" ")
            print(str(grid[row][col]), end=" ")
    print("")


def run_langton(rules, size):
    if size == 1:
        return(1, [[1]])
    elif size == 0:
        return(0, [])
    row, col = size, size
    grid = [[0 for i in range(col)] for j in range(row)]
    antpos = [size // 2, size // 2]
    grid[antpos[0]][antpos[0]] = 1
    dir = [0, 1, 2, 3]  # North, East, South, West
    antpos = [antpos[0] - 1,antpos[1]]
    count = 1
    color = grid[antpos[0] - 1][antpos[1]]
    if rules[color] == "R":
        antdir = dir[(color + 1) % 4]
    if rules[color] == "L":
        antdir = dir[(color - 1) % 4]
    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)
    while True:
        try:
            if rules[color] == "R":
                if (antdir == 0 or antdir == -4) and rules[color] == "R":
                    color = grid[(antpos[0] - 1)][antpos[1]]
                    antpos = [antpos[0] - 1, antpos[1]]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)

                elif (antdir == 1 or antdir == -3) and rules[color] == "R":
                    color = grid[(antpos[0])][antpos[1] + 1]
                    antpos = [antpos[0], antpos[1] + 1]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)

                elif (antdir == 2 or antdir == -2) and rules[color] == "R":
                    color = grid[(antpos[0]) + 1][antpos[1]]
                    antpos = [antpos[0] + 1, antpos[1]]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)

                elif (antdir == 3 or antdir == -1) and rules[color] == "R":
                    color = grid[(antpos[0])][antpos[1] - 1]
                    antpos = [antpos[0], antpos[1] - 1]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)
            if rules[color] == "L":
                if (antdir == 0 or antdir == -4) and rules[color] == "L":
                    color = grid[(antpos[0] - 1)][antpos[1]]
                    antpos = [antpos[0] - 1, antpos[1]]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)

                elif (antdir == 1 or antdir == -3) and rules[color] == "L":
                    color = grid[(antpos[0])][antpos[1] + 1]
                    antpos = [antpos[0], antpos[1] + 1]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)

                elif (antdir == 2 or antdir == -2) and rules[color] == "L":
                    color = grid[(antpos[0]) + 1][antpos[1]]
                    antpos = [antpos[0] + 1, antpos[1]]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)

                elif (antdir == 3 or antdir == -1) and rules[color] == "L":
                    color = grid[(antpos[0])][antpos[1] - 1]
                    antpos = [antpos[0], antpos[1] - 1]
                    count += 1
                    if rules[color] == "R":
                        antdir = (antdir + 1) % 4
                    if rules[color] == "L":
                        antdir = (antdir - 1) % 4
                    if antpos[0] < 0 or antpos[1] < 0:
                        return (count, grid)
                    grid[antpos[0]][antpos[1]] = (grid[antpos[0]][antpos[1]] + 1) % len(rules)

        except IndexError:
            return(count + 1, grid)
