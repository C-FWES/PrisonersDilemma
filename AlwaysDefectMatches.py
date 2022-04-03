rounds = 10

#intialize matchups
from AlwaysCooperate import always_cooperate
from AlwaysDefect import always_defect
from Grudger import grudgy
from NaiveProber import naive_prober
from RemorsefulProber import remorseful_prober
from SuspiciousTitForTat import mean_tit_for_tat
from TitForTat import tit_for_tat

def match_A1():
    a = always_defect()
    b = always_cooperate()
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
    print("ALWAYS DEFECT: " + str(a.score))
    print("ALWAYS COOPERATE: " + str(b.score))
    print('------------------------------')

def match_B1():
    a = always_defect()
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
    print("ALWAYS DEFECT: " + str(a.score))
    print("NAIVE PROBER: " + str(b.score))
    print('------------------------------')

def match_C1():
    a = always_defect()
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
    print("ALWAYS DEFECT: " + str(a.score))
    print("GRUDGER: " + str(b.score))
    print('------------------------------')

def match_D1():
    a = always_defect()
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
    print("ALWAYS DEFECT: " + str(a.score))
    print("REMORSEFUL PROBER: " + str(b.score))
    print('------------------------------')

def match_E1():
    a = always_defect()
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
    print("ALWAYS DEFECT: " + str(a.score))
    print("SUSPICIOUS TIT FOR TAT: " + str(b.score))
    print('------------------------------')

def match_F1():
    a = always_defect()
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
    print("ALWAYS DEFECT: " + str(a.score))
    print("TIT FOR TAT: " + str(b.score))
    print("END OF SET")
    print('------------------------------')