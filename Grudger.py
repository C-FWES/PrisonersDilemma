#He will cooperate and then if you are meany he will be angry
from Entity import Player

class grudgy(Player):
    def strategy(self, memory: list, own_memory=[]):
        if 0 not in memory:
            return 1
        return 0