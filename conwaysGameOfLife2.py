import random
ninput = open("player1.txt", "r")
player1List = ninput.readlines()
ninput.close()

linput = open("player2.txt", "r")
player2List = linput.readlines()
linput.close()

player1coord = []
for coord in player1List:
    lst = coord.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    player1coord.append(lst)

player2coord = []
for coord in player2List:
    lst2 = coord.split()
    for i in range(len(lst2)):
        lst2[i] = int(lst2[i])
    player2coord.append(lst2)

grid = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    grid.append(row)

for row, col in player1coord:
    grid[row][col] = 1

for row, col in player2coord:
    grid[row][col] = 2

#CREATOR function makes a grid based on data provided previously.
#It takes in input as a 2-dimensional list.
def CREATOR(grid):
    print("  ", end = "")
    for i in range(len(grid)):
        print(str(i) + " ", end = "")
    print("")
    for i in range(len(grid)):
        print(i, end = "")
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                print(" -", end = "")
            elif grid[i][j] == 1:
                print(" O", end = "")
            else:
                print(" X", end = "")
        print("")

#returns the number of a specific number within a grid
#used to find the different player counts
def findAndCount(grid, int):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == int:
                count += 1
    return count

#neighbor function takes the coordinates of a cell and uses
#the game rules to decide if the cell lives or dies.
def neighbor(row, col):
    countO = 0
    countX = 0
    #checking if the surrounding cells are alive or dead
    if row - 1 >= 0 and grid[row-1][col] == 1:
        countO += 1
    elif row - 1 >= 0 and grid[row-1][col] == 2:
        countX += 1
    
    if row - 1 >= 0 and col + 1 < len(grid[row]) and grid[row-1][col+1] == 1:
        countO += 1
    elif row - 1 >= 0 and col + 1 < len(grid[row]) and grid[row-1][col+1] == 2:
        countX += 1
    
    if col + 1 < len(grid[row]) and grid[row][col+1] == 1:
        countO += 1
    elif col + 1 < len(grid[row]) and grid[row][col+1] == 2:
        countX += 1
    
    if row + 1 < len(grid) and col + 1 < len(grid[row]) and grid[row+1][col+1] == 1:
        countO += 1
    elif row + 1 < len(grid) and col + 1 < len(grid[row]) and grid[row+1][col+1] == 2:
        countX += 1
    
    if row + 1 < len(grid) and grid[row+1][col] == 1:
        countO += 1
    elif row + 1 < len(grid) and grid[row+1][col] == 1:
        countX += 1
    
    if row + 1 < len(grid) and col - 1 > 0 and grid[row+1][col-1] == 1:
        countO += 1
    elif row + 1 < len(grid) and col - 1 > 0 and grid[row+1][col-1] == 2:
        countX += 1
    
    if col - 1 > 0 and grid[row][col-1] == 1:
        countO += 1
    elif col - 1 > 0 and grid[row][col-1] == 2:
        countX += 1
    
    if row - 1 > 0 and col - 1 > 0 and grid[row-1][col-1] == 1:
        countO += 1
    elif row - 1 > 0 and col - 1 > 0 and grid[row-1][col-1] == 2:
        countX += 1
    
    #determining whether the current cell lives or dies
    
    #these are for when the cell is alive
    #but has too few living cells around it
    if countO < 2 and grid[row][col] == 1:
        grid[row][col] = 0
    elif countX < 2 and grid[row][col] == 2:
        grid[row][col] = 0
    
    #these are for if the cell is alive
    #but has too many living cells around it
    if countO > 3 and grid[row][col] == 1:
        grid[row][col] = 0
    elif countX > 3 and grid[row][col] == 2:
        grid[row][col] = 0
    
    #these are for when the cell is already dead
    #but based on the number of living cells around it
    #will either become an X or and O
    if countX == 3 and countO == 3 and grid[row][col] == 0:
        num = random.randint(1,2)
        grid[row][col] = num
    elif countO == 3 and grid[row][col] == 0:
        grid[row][col] = 1
    elif countX == 3 and grid[row][col] == 0:
        grid[row][col] = 2

while True:
    CREATOR(grid)

    playerOcount = findAndCount(grid, 1)
    playerXcount = findAndCount(grid, 2)
    
    print("Player O's turn")
    rowToAddO = input("Which row is the cell you want to add in: ")
    colToAddO = input("Which column is the cell you want to add in: ")
    rowToRemoveO = input("Which row is the cell you want to remove in: ")
    colToRemoveO = input("Which column is the cell you want to remove in: ")
    grid[int(rowToAddO)][int(colToAddO)] = 1
    grid[int(rowToRemoveO)][int(colToRemoveO)] = 0

    print("Player X's turn")
    rowToAddX = input("Which row is the cell you want to add in: ")
    colToAddX = input("Which column is the cell you want to add in: ")
    rowToRemoveX = input("Which row is the cell you want to remove in: ")
    colToRemoveX = input("Which column is the cell you want to remove in: ")
    grid[int(rowToAddX)][int(colToAddX)] = 2
    grid[int(rowToRemoveX)][int(colToRemoveX)] = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            neighbor(row, col)

