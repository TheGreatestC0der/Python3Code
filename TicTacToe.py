#AM14 Project 1: Tic Tac Toe UI
#Create a one-player Tic Tac Toe game. 
#The program should first randomly select whether the human player or the computer player gets to go first.
#Every time that someone takes a turn, be sure to update the grid afterwards.
#Your game should be able to determine when somebody wins or when there is a tie.
#In this project, the computer player should simply choose a random location among the ones that are remaining.

#The coin flip shows that you (X) will go first!
#Press Enter to begin!
#   |   |  
#-––+–––+–––
#   |   |  
#-––+–––+–––
#   |   |  

#Pick a row to play: 1
#Pick a column to play: 1
#   |   |  
#-––+–––+–––
#   | X |  
#-––+–––+–––
#   |   |  

# O |   |  
#-––+–––+–––
#   | X |  
#-––+–––+–––
#   |   |  

#Pick a row to play: 0
#Pick a column to play: 1
# O | X |  
#-––+–––+–––
#   | X |  
#-––+–––+–––
#   |   |  

# O | X |  
#-––+–––+–––
#   | X |  
#-––+–––+–––
# O |   |  

#Pick a row to play: 1
#Pick a column to play: 0
# O | X |  
#-––+–––+–––
# X | X |  
#-––+–––+–––
# O |   |  

# O | X |  
#-––+–––+–––
# X | X |  
#-––+–––+–––
# O | O |  

#Pick a row to play: 1
#Pick a column to play: 2
# O | X |  
#-––+–––+–––
# X | X | X
#-––+–––+–––
# O | O |  

#Wow! You won!

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

count = 0
while True:
    if count == 0:
        CREATOR(grid)
    player_1_row = int(input("Player 1, which row is the spot you want to mark in? "))
    player_1_col = int(input("Which column is the spot you want to mark in? "))
    if grid[player_1_row][player_1_col] == " ":
        grid[player_1_row][player_1_col] = 1
    else:
        print("That spot's taken...")
    CREATOR(grid)
    if CHECK_WIN(grid) == 1:
        print("Player 1 wins!")
        break
    elif CHECK_WIN(grid) == 0:
        print("It's a tie!")
        break

    player_2_row = int(input("Player 2, which row is the spot you want to mark in? "))
    player_2_col = int(input("Which column is the spot you want to mark in? "))
    if grid[player_2_row][player_2_col] == " ":
        grid[player_2_row][player_2_col] = 2
    else:
        print("That spot's taken...")
    CREATOR(grid)
    if CHECK_WIN(grid) == 2:
        print("Player 2 wins!")
        break
    elif CHECK_WIN(grid) == 0:
        print("It's a tie!")
        break
    count += 1