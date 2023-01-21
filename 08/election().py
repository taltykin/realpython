
from random import random

# def elect(probability):
#     if random.random() < probability:
#         return "tails"
#     else:
#         return "heads"

# head_tally = 0
# tails_tally = 0

# for n in range(1000):
#     if elect(.7) == "tails":
#         tails_tally = tails_tally + 1
#     else:
#         head_tally = head_tally + 1

# print(head_tally)
# print(tails_tally)


def elect():

    totally_A = 0
    totally_B = 0

    for i in range(0, 10000):
        votes_a = 0
        votes_b = 0
        if random() < .87:
            votes_a = votes_a + 1
        else:
            votes_b = votes_b + 1

        if random() < .65:
            votes_a = votes_a + 1
        else:
            votes_b = votes_b + 1

        if random() < .17:
            votes_a = votes_a + 1
        else:
            votes_b = votes_b + 1
        if votes_a > votes_b:
            totally_A = totally_A + 1
        else:
            totally_B = totally_B + 1 
    
    print(totally_A)
    print(totally_B)

elect()