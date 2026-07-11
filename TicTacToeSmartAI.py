import math
import random

def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                if col == len(board[row]) - 1:
                    print("O")
                else:
                    print("O", end = "")
                    print(" | ", end = "")
            elif board[row][col] == 2:
                if col == len(board[row]) - 1:
                    print("X")
                else:
                    print("X", end = "")
                    print(" | ", end = "")
            else:
                if col == len(board[row]) - 1:
                    print(" ")
                else:
                    print(" ", end = "")
                    print(" | ", end = "")
        if row < 2:
            print("--+---+--")

def is_winner(board, player):
    #Checks the 3x3 board to determine if the specified player has won.
    #You should check all 3 horizontal rows, 3 vertical columns, and 2 diagonals.
    
    #Parameters:
    #board (list): The current game board.
    #player (str): 'X' or 'O'.
    
    #Returns:
    #bool: True if the player has won, False otherwise.

def is_board_full(board):
    #Checks if there are any remaining playable spaces left on the board.
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == " ":
                return False
    return True
    #Parameters:
    #board (list): The current game board.
    
    #Returns:
    #bool: True if no spaces are empty (' '), False otherwise.

def get_available_moves(board):
    #Finds all empty positions on the current board.
    moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == " ":
                moves.append(row * 3 + col)
    #Parameters:
    #board (list): The current game board.
    
    #Returns:
    #list: A list of integers (0-8) representing the indices of empty spaces.

def minimax(board, is_maximizing):
    #The core recursive algorithm. It plays out every possible future combination 
    #of the game to score the current board state.
    
    # - Base Cases: Check if 'X' won (+1), 'O' won (-1), or the board is full (0).
    # - If is_maximizing is True: Loop through available moves, temporarily place 'X',
      #recursively call minimax with is_maximizing=False, track the highest score,
      #and undo the move.
    #- If is_maximizing is False: Loop through available moves, temporarily place 'O',
      #recursively call minimax with is_maximizing=True, track the lowest score,
      #and undo the move.
    
    #Parameters:
    #board (list): The simulated game board.
    #is_maximizing (bool): True if it's the AI's turn (MAX), False if it's the human's (MIN).
    
    #Returns:
    #int: The optimal score (-1, 0, or 1) from this board branch.

def find_best_move(board):
    #The entry point for the AI's turn. It looks at the current board, evaluates 
    #the immediate next valid moves using minimax(), and picks the move index that
    #results in the highest score.
    
    #Parameters:
    #board (list): The actual current game board.
    
    #Returns:
    #int: The best index (0-8) for the AI to play.


#The main game loop. Initializes a blank board (9 spaces of ' '), tracks whose 
#turn it is, handles user keyboard input, calls find_best_move() when it is the 
#AI's turn, updates the board, and prints the result when a terminal state is reached.