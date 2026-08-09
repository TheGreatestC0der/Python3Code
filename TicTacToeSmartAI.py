import math
import random

def print_board(board):
    #Prints the current state of the board in a 3x3 grid format.
    for row in range(3):
        for col in range(3):
            if col == 2:
                print(board[row * 3 + col])
            else:
                print(board[row * 3 + col], end=" | ")
        if row < 2:
            print("--+---+--")
    #Parameters:
    #board (list): The current game board.

def is_winner(board, player):
    #Checks the 3x3 board to determine if the specified player has won.
    #You should check all 3 horizontal rows, 3 vertical columns, and 2 diagonals.
    for row in range(3):
        if all(board[row * 3 + col] == player for col in range(3)):
            return True
    for col in range(3):
        if all(board[row * 3 + col] == player for row in range(3)):
                return True
    if all(board[i * 3 + i] == player for i in range(3)):
        return True
    if all(board[i * 3 + (2-i)] == player for i in range(3)):
        return True
    #Parameters:
    #board (list): The current game board.
    #player (str): 'X' or 'O'.
    
    #bool: True if the player has won, False otherwise.

def is_board_full(board):
    #Checks if there are any remaining playable spaces left on the board.
    for space in board:
        if space == " ":
            return False
    return True
    #Parameters:
    #board (list): The current game board.
    
    #Returns:
    #bool: True if no spaces are empty (' '), False otherwise.

def get_available_moves(board):
    #Finds all empty positions on the current board.
    moves = []
    for i in range(len(board)):
        if board[i] == " ":
            moves.append(i)
    return moves
    #Parameters:
    #board (list): The current game board.
    
    #Returns:
    #list: A list of integers (0-8) representing the indices of empty spaces.

def minimax(board, is_maximizing):
    #The core recursive algorithm. It plays out every possible future combination 
    #of the game to score the current board state.
    # - Base Cases: Check if 'X' won (-1), 'O' won (+1), or the board is full (0).
    if is_winner(board, "X"):
        return -1  # 'X' wins
    if is_winner(board, "O"):
        return 1  # 'O' wins
    if is_board_full(board):
        return 0  # Tie
    # - If is_maximizing is True: Loop through available moves, temporarily place 'O',
      #recursively call minimax with is_maximizing=False, track the highest score,
      #and undo the move.
    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "

            if best_score < score:
                best_score = score

    #- If is_maximizing is False: Loop through available moves, temporarily place 'X',
      #recursively call minimax with is_maximizing=True, track the lowest score,
      #and undo the move.
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "

            if best_score > score:
                best_score = score
        
    
    return best_score
    #Parameters:
    #board (list): The simulated game board.
    #is_maximizing (bool): True if it's the AI's turn (MAX), False if it's the human's (MIN).
    
    #Returns:
    #int: The optimal score (-1, 0, or 1) from this board branch.

def find_best_move(board):
    #The entry point for the AI's turn. It looks at the current board, evaluates 
    #the immediate next valid moves using minimax(), and picks the move index that
    #results in the highest score.
    pos_moves = get_available_moves(board)  # Get the list of available moves
    
    best_score = -math.inf
    best_move = (0, 0)
    for move in pos_moves:
        board[move] = "O"
        minimax_score = minimax(board, False)  # Evaluate the move using minimax
        board[move] = " "

        if minimax_score > best_score:
            best_score = minimax_score
            best_move = move  # Convert index to (row, col)

    #Parameters:
    #board (list): The actual current game board.
    
    #Returns:
    #int: The best index (0-8) for the AI to play.
    return best_move  # Convert (row, col) back to index

#The main game loop. Initializes a blank board (9 spaces of ' '), tracks whose 
#turn it is, handles user keyboard input, calls find_best_move() when it is the 
#AI's turn, updates the board, and prints the result when a terminal state is reached.
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
turn = "X"
print_board(board)
while True:    
    if turn == "O":
        best_move_index = find_best_move(board)
        board[best_move_index] = "O"
        turn = "X"
        print_board(board)
    else:
        player_row = int(input("Player, which row is the spot you want to mark in? "))
        player_col = int(input("Which column is the spot you want to mark in? "))
        if board[player_row * 3 + player_col] == " ":
            board[player_row * 3 + player_col] = "X"
        else:
            print("That spot's taken...")
        print_board(board)
        turn = "O"

    if is_winner(board, "X"):
        print("Player 1 wins!")
        break
    elif is_winner(board, "O"):
        print("Computer wins!")
        break
    elif is_board_full(board):
        print("It's a tie!")
        break