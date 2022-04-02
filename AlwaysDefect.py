#Always meany
from Entity import Player

class always_defect(Player):
    def strategy(self, memory: list, own_memory=[]):
        return 0