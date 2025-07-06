import os
import random
import sys
from tic_tac_toe import tic_tac_toe

sys.path.append('../')


if __name__ == "__main__":
    plateau, _ = tic_tac_toe.TicTacToe.start_game()
    start = 0
    play = True
    list_moves = []
    while play:
        player = tic_tac_toe.TicTacToe.select_player(start, list_moves)
        plateau = tic_tac_toe.TicTacToe.make_move(plateau, player)
        start += 1
        if tic_tac_toe.TicTacToe.check_board(plateau):
            play = tic_tac_toe.TicTacToe().restart_game()
        else:
            pass

    #for i in range(0, 10):
    #    player = tic_tac_toe.TicTacToe.select_player(i, list_moves)
    #    plateau = tic_tac_toe.TicTacToe.make_move(plateau, player)
    #    if tic_tac_toe.TicTacToe.check_board(plateau):
    #        break
    #tic_tac_toe.TicTacToe().restart_game()

