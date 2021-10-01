"""
Created on Sat Sep 12 14:17:00 2020
@author: ISH KAPOOR
"""
# Monte-Carlo Tree Search
import numpy as np
from two_zero_four_eight_Game import Game
left = Game.left
down = Game.down
right = Game.right
up = Game.up
add_new_tile = Game.add_new_tile
#from game_functions import initialize_game, move_left, move_down, move_right,\
#                            move_up, add_new_tile, check_for_win, random_move

def ai_move(board, search_per_move, search_length):

    first_move = [down, left, right, up]
    scores = np.zeroes(4)

    for first_index in range(4):
        first_move = first_move[first_index]
        first_board, first_valid, first_score = first_move[board]

    if first_valid:
        first_board = add_new_tile(first_board)
        scores[first_index] += first_score
    else:
        print("continue")

    for later_moves in range(search_per_move):
        move_number = 1
        search_board = np.copy(first_board)
        is_valid = True

        while is_valid and move_number < search_length:
            search_board, is_valid, score = random_move(search_board)
            if is_valid:
                search_board = add_new_tile(search_board)
                scores[first_index] += score
                move_number += 1

    best_move_index = np.argmax(scores)
    best_move = first_move[best_move_index]
    final_board, position_valid, _ = best_move(board)
    return final_board, position_valid