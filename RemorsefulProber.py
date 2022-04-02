#like naive probber, has long memoruy , remembers if it did a random defection so he is sad and he lets the other one hit him back
import random

from Entity import Player

class remorseful_prober(Player):
    def strategy(self, memory: list, own_memory: list):
        if not memory:
            return 1
        random_number = random.randint(0, 10)
        if random_number == 3:
            return 0
        if own_memory[-1] == 0:
            return 1
        return memory[-1]