import itertools
import random
import warnings

from collections import namedtuple

from isolation import Board 

from game_agent import MinimaxPlayer
from isolation import Board
from sample_players import improved_score


player1 = MinimaxPlayer(search_depth=100)
player2 = MinimaxPlayer(search_depth=100)
game = Board(player1, player2)

def timer():
    return 10.0

while game.get_legal_moves() != 0:
    print("I did a turn")
    # DO this stuff
    player = game.active_player
    move = player.get_move(game, timer)
    game.apply_move(move)
    print(game.to_string())