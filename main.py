import os
import random
import sys
from tic_tac_toe import tic_tac_toe

sys.path.append('../')


if __name__ == "__main__":
    plateau = tic_tac_toe.TicTacToe.start_game()
    start = 0
    list_moves = []
    tic_tac_toe.TicTacToe.select_player(start, list_moves)
    for i in range(0, 10):
        player = tic_tac_toe.TicTacToe.select_player(i, list_moves)
        plateau = tic_tac_toe.TicTacToe.make_move(plateau, player)
        tic_tac_toe.TicTacToe.check_board(plateau)
    tic_tac_toe.TicTacToe.restart_game()

