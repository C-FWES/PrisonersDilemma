#tit for tat, but 1/10 randmoly throws in defection
import random

from Entity import Player

class naive_prober(Player):
    def strategy(self, memory: list, own_memory=[]):
        if not memory:
            return 1
        random_number = random.randint(0, 10)
        if random_number == 3:
            return 0
        return memory[-1]
