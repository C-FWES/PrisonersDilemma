#He start being friendly and then he will copy the other person
from Entity import Player

class tit_for_tat(Player):
    def strategy(self, memory: list, own_memory=[]):
        if not memory:
            return 1
        return memory[-1]
