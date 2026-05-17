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
CREATOR(grid)


