# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_cli.ipynb (unless otherwise specified).

__all__ = ['play']

# Cell
from .game import init_player, game_loop
from fastcore.script import call_parse, Param

# Cell
@call_parse
def play(n: Param("The number of enemies you want to encounter.", int) = 10):
    player = init_player()
    game_loop(player, n)