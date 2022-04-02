#Always nice
from Entity import Player

class always_cooperate(Player):
    def strategy(self, memory: list, own_memory=[]):
        return 1
