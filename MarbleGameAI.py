import math
import random

marble_num = 8

turn = "Player"

def get_available_moves(marble_num):
    #Returns a list of valid moves (1, 2, or 3) based on the current number of marbles.
    if marble_num >= 3:
        return [1, 2, 3]
    else:
        if marble_num == 2:
            return [1, 2]
        elif marble_num == 1:
            return [1]

def minimax(marble_num, is_maximizing):


def find_best_move(marble_num):

while True:
    if turn == "AI":
        #blah blah blah
    else:
        player_num = int(input("Player, how many marbles do you want to take? (1-3) "))
        marble_num -= player_num
        print(f"Marbles left: {marble_num}")
        turn = "AI"