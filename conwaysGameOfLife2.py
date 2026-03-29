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
CREATOR(grid)