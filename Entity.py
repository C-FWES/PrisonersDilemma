class Player ():
    def __init__(self):
        self.score = 0
        self.memory = []
        self.own_memory = [-1]

    def strategy(self, memory: list, own_memory: list):
        return 1