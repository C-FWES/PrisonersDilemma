rounds = 10

#intialize matchups
from AlwaysCooperate import always_cooperate
from AlwaysDefect import always_defect
from Grudger import grudgy
from NaiveProber import naive_prober
from RemorsefulProber import remorseful_prober
from SuspiciousTitForTat import mean_tit_for_tat
from TitForTat import tit_for_tat

def match_A():
    a = always_cooperate()
    b = always_defect()
    r = rounds
    a_memory = []
    b_memory = []
    while (r > 0):
        a_action = a.strategy(a.memory)
        b.memory.append(a_action)
        b_action = b.strategy(b.memory)
        if a_action == 1 and b_action == 1:
            a.score += 3
            b.score += 3
        if a_action == 0 and b_action == 1:
            a.score += 5
            b.score += 0
        if a_action == 1 and b_action == 0:
            a.score += 0
            b.score += 5
        if a_action == 0 and b_action == 0:
            a.score += 1
            b.score += 1
        r-=1
    print("ALWAYS COOPERATE: " + str(a.score))
    print("ALWAYS DEFECT: " + str(b.score))
    print('------------------------------')

match_A()

def match_B():
    a = always_cooperate()
    b = naive_prober()
    r = rounds
    a_memory = []
    b_memory = []
    while (r > 0):
        a_action = a.strategy(a.memory)
        b.memory.append(a_action)
        b_action = b.strategy(b.memory)
        if a_action == 1 and b_action == 1:
            a.score += 3
            b.score += 3
        if a_action == 0 and b_action == 1:
            a.score += 5
            b.score += 0
        if a_action == 1 and b_action == 0:
            a.score += 0
            b.score += 5
        if a_action == 0 and b_action == 0:
            a.score += 1
            b.score += 1
        r-=1
    print("ALWAYS COOPERATE: " + str(a.score))
    print("NAIVE PROBER: " + str(b.score))
    print('------------------------------')

match_B()

def match_C():
    a = always_cooperate()
    b = grudgy()
    r = rounds
    a_memory = []
    b_memory = []
    while (r > 0):
        a_action = a.strategy(a.memory)
        b.memory.append(a_action)
        b_action = b.strategy(b.memory)
        if a_action == 1 and b_action == 1:
            a.score += 3
            b.score += 3
        if a_action == 0 and b_action == 1:
            a.score += 5
            b.score += 0
        if a_action == 1 and b_action == 0:
            a.score += 0
            b.score += 5
        if a_action == 0 and b_action == 0:
            a.score += 1
            b.score += 1
        r-=1
    print("ALWAYS COOPERATE: " + str(a.score))
    print("GRUDGER: " + str(b.score))
    print('------------------------------')

match_C()

def match_D():
    a = always_cooperate()
    b = remorseful_prober()
    r = rounds
    a_memory = []
    b_memory = []
    b_own_memory = []
    while (r > 0):
        a_action = a.strategy(a.memory)
        b.memory.append(a_action)
        b_action = b.strategy(b.memory, b.own_memory)
        b.own_memory.append(b_action)
        if a_action == 1 and b_action == 1:
            a.score += 3
            b.score += 3
        if a_action == 0 and b_action == 1:
            a.score += 5
            b.score += 0
        if a_action == 1 and b_action == 0:
            a.score += 0
            b.score += 5
        if a_action == 0 and b_action == 0:
            a.score += 1
            b.score += 1
        r-=1
    print("ALWAYS COOPERATE: " + str(a.score))
    print("REMORSEFUL PROBER: " + str(b.score))
    print('------------------------------')

match_D()

def match_E():
    a = always_cooperate()
    b = mean_tit_for_tat()
    r = rounds
    a_memory = []
    b_memory = []
    while (r > 0):
        a_action = a.strategy(a.memory)
        b.memory.append(a_action)
        b_action = b.strategy(b.memory)
        if a_action == 1 and b_action == 1:
            a.score += 3
            b.score += 3
        if a_action == 0 and b_action == 1:
            a.score += 5
            b.score += 0
        if a_action == 1 and b_action == 0:
            a.score += 0
            b.score += 5
        if a_action == 0 and b_action == 0:
            a.score += 1
            b.score += 1
        r-=1
    print("ALWAYS COOPERATE: " + str(a.score))
    print("SUSPICIOUS TIT FOR TAT: " + str(b.score))
    print('------------------------------')

match_E()

def match_F():
    a = always_cooperate()
    b = tit_for_tat()
    r = rounds
    a_memory = []
    b_memory = []
    while (r > 0):
        a_action = a.strategy(a.memory)
        b.memory.append(a_action)
        b_action = b.strategy(b.memory)
        if a_action == 1 and b_action == 1:
            a.score += 3
            b.score += 3
        if a_action == 0 and b_action == 1:
            a.score += 5
            b.score += 0
        if a_action == 1 and b_action == 0:
            a.score += 0
            b.score += 5
        if a_action == 0 and b_action == 0:
            a.score += 1
            b.score += 1
        r-=1
    print("ALWAYS COOPERATE: " + str(a.score))
    print("TIT FOR TAT: " + str(b.score))
    print('------------------------------')

match_F()