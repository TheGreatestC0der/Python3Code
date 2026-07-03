#The AI should:
#Play a winning move if there is one,
#Play a move that blocks a winning move from the opponent, or
#Play center if it is open.
#To do this, create a function that tests if a move is a winning move.
#Create a duplicate board each time so the test move does not affect the actual board.

import random

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

def CHECK_WIN(table):
    count = 0
    if table[0][0] == table[0][1] == table[0][2] != " ":
        return table[0][0]
    elif table[1][0] == table[1][1] == table[1][2] != " ":
        return table[1][0]
    elif table[2][0] == table[2][1] == table[2][2] != " ":
        return table[2][0]
    elif table[0][0] == table[1][0] == table[2][0] != " ":
        return table[0][0]
    elif table[0][1] == table[1][1] == table[2][1] != " ":
        return table[0][1]
    elif table[0][2] == table[1][2] == table[2][2] != " ":
        return table[0][2]
    elif table[0][0] == table[1][1] == table[2][2] != " ":
        return table[0][0]
    elif table[0][2] == table[1][1] == table[2][0] != " ":
        return table[0][2]
    else:
        for row in range(len(table)):
            for col in range(len(table[row])):
                if table[row][col] != " ":
                    count += 1
        if count == 9:
            return 0
        else:
            return -1

#creates a copy of a grid for testing purposes
def copy(grid):
    gridTemp = []
    for row in range(len(grid)):
        rows = []
        for col in range(len(grid[row])):
            rows.append(grid[row][col])
        gridTemp.append(rows)
    return gridTemp

#determines all possible moves the computer could make at the time
#this counts as all future player moves since the computer
#might have to spend a move blocking the player's winning move
def pos_moves(tableTwo):
    movesList = []
    for x in range(len(tableTwo)):
        for y in range(len(tableTwo[x])):
            if tableTwo[x][y] == " ":
                movesList.append([x,y])
    return movesList

#both functions determine if a move is a winning move
#returns either True or False
def win_move_computer(tableTwo):
    if CHECK_WIN(tableTwo) == 2:
        return True
    else:
        return False
def win_move_player(tableTwo):
    if CHECK_WIN(tableTwo) == 1:
        return True
    else:
        return False

count = 0
while True:
    if count == 0:
        CREATOR(grid)
    
    #player code for game
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
    
    #computer code and thought process
    movesList = pos_moves(grid)
    for x,y in movesList:
        gridTemp = copy(grid)
        gridTemp[x][y] = 2
        check = False
        #if the computer has a winning move it will immediately
        #pick that move first
        if win_move_computer(gridTemp) == True:
            grid[x][y] = 2
            print("win")
            CREATOR(grid)
            break
            
        #if the player has a winning move, the computer will block it
        gridTemp[x][y] = 1
        if win_move_player(gridTemp) == True:
            grid[x][y] = 2
            print("block")
            CREATOR(grid)
            break
            
        #if there is no winning move the computer checks the center
        #if it is open it takes it
        if grid[1][1] == " ":
            grid[1][1] = 2
            print("center")
            CREATOR(grid)
            break
            
        #if there are no winning moves and the center is taken
        #the computer will pick randomly from its existing possible moves
        else:
            while True:
                randomRow = random.randint(0, 2)
                randomCol = random.randint(0, 2)
                if grid[randomRow][randomCol] != " ":
                    pass
                else:
                    grid[randomRow][randomCol] = 2
                    print("random")
                    CREATOR(grid)
                    print(grid)
                    check = True
                    break
        if check:
            break

    #for the computer we don't need to check whether a spot is taken
    #as it only considers moves for spots that are empty
    if CHECK_WIN(grid) == 2:
        print("The computer wins!")
        break
    elif CHECK_WIN(grid) == 0:
        print("It's a tie!")
        break
    count += 1
                
    
