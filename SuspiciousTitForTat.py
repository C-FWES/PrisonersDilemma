#Hes like tit for tat but he is mean for the first move
from Entity import Player

class mean_tit_for_tat(Player):
    def strategy(self, memory: list, own_memory=[]):
        if not memory:
            return 0
        return memory[-1]
