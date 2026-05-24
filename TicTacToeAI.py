grid = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    grid.append(row)

def CREATOR(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if col == len(grid[row]) - 1:
                    print("O")
                else:
                    print("O", end = "")
                    print(" | ", end = "")
            elif grid[row][col] == 2:
                if col == len(grid[row]) - 1:
                    print("X")
                else:
                    print("X", end = "")
                    print(" | ", end = "")
            else:
                if col == len(grid[row]) - 1:
                    print(" ")
                else:
                    print(" ", end = "")
                    print(" | ", end = "")
        if row < 2:
            print("--+---+--")

def CHECK_WIN(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    if row + 2 < len(grid) and grid[row + 2][col] == 1:
                        return 1
                elif col + 1 < len(grid[row]) and grid[row][col + 1] == 1:
                    if col + 2 < len(grid[row]) and grid[row][col + 2] == 1:
                        return 1
                elif row + 1 < len(grid) and col + 1 < len(grid[row]) and grid[row + 1][col + 1] == 1:
                    if row + 2 < len(grid) and col + 2 < len(grid[row]) and grid[row + 2][col + 2] == 1:
                        return 1
                elif row - 1 > 0 and col + 1 < len(grid[row]) and grid[row - 1][col + 1] == 1:
                    if row - 2 > 0 and col + 2 < len(grid[row]) and grid[row - 2][col + 2] == 1:
                        return 1
            elif grid[row][col] == 2:
                if row + 1 < len(grid) and grid[row + 1][col] == 2:
                    if row + 2 < len(grid) and grid[row + 2][col] == 2:
                        return 2
                elif col + 1 < len(grid[row]) and grid[row][col + 1] == 2:
                    if col + 2 < len(grid[row]) and grid[row][col + 2] == 2:
                        return 2
                elif row + 1 < len(grid) and col + 1 < len(grid[row]) and grid[row + 1][col + 1] == 2:
                    if row + 2 < len(grid) and col + 2 < len(grid[row]) and grid[row + 2][col + 2] == 2:
                        return 2
                elif row - 1 > 0 and col + 1 < len(grid[row]) and grid[row - 1][col + 1] == 2:
                    if row - 2 > 0 and col + 2 < len(grid[row]) and grid[row - 2][col + 2] == 2:
                        return 2
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != " ":
                count += 1
    if count == 9:
        return 0

def computer(grid):
    

while True:
    if count == 0:
        CREATOR(grid)
    player_row = int(input("Player, which row is the spot you want to mark in? "))
    player_col = int(input("Which column is the spot you want to mark in? "))
    if grid[player_row][player_col] == " ":
        grid[player_row][player_col] = 1
    else:
        print("That spot's taken...")
    CREATOR(grid)
    if CHECK_WIN(grid) == 1:
        print("Player 1 wins!")
        break
    elif CHECK_WIN(grid) == 0:
        print("It's a tie!")
        break
    
