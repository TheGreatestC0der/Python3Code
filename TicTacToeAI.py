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
def pos_moves(gridTemp):
    movesList = []
    for row in range(len(gridTemp)):
        rows = []
        for col in range(len(gridTemp[row])):
            if gridTemp[row][col] == " ":
                rows.append(col)
        movesList.append(rows)
    return movesList

#both functions determine if a move is a winning move
#returns either True or False
def win_move_computer(movesList, row, col):
    movesList[row][col] = 2
    if CHECK_WIN(gridTemp) == 2:
        return True
    else:
        return False
def win_move_player(movesList, row, col):
    movesList[row][col] = 1
    if CHECK_WIN(gridTemp) == 1:
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
    gridTemp = copy(grid)
    movesList = pos_moves(gridTemp)
    for row in range(len(movesList)):
        for col in range(len(movesList[row])):
            
            #if the computer has a winning move it will immediately
            #pick that move first
            if win_move_computer(movesList, row, col):
                grid[row][col] = 2
            
            #if the player has a winning move, the computer will block it
            elif win_move_player(movesList, row, col):
                grid[row][col] = 2
            
            #if there is no winning move the computer checks the center
            #if it is open it takes it
            elif grid[1][1] == " ":
                grid[1][1] = 2
            
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

    #for the computer we don't need to check whether a spot is taken
    #as it only considers moves for spots that are empty
    if CHECK_WIN(grid) == 2:
        print("The computer wins!")
        break
    elif CHECK_WIN(grid) == 0:
        print("It's a tie!")
        break
    count += 1
                
    
