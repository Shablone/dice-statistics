#%%
from src.board_statistics import Board_Statistics
from src.dice import Die, FairDie, UnfairDie
#%%
Board_Statistics().add_highest([FairDie(12),FairDie(12)]).plot()
Board_Statistics().add_die(FairDie(12)).plot()
# %%
Board_Statistics() \
    .add_highest([FairDie(6),FairDie(6)]) \
    .add_highest([FairDie(6),FairDie(6)]) \
    .plot()

Board_Statistics() \
    .add_die(FairDie(6)) \
    .add_die(FairDie(6)) \
    .plot()
# %%