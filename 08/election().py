
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
        if random() < .87:
            totally_A = totally_A + 1
        else:
            totally_B = totally_B + 1

        if random() < .65:
            totally_A = totally_A + 1
        else:
            totally_B = totally_B + 1

        if random() < .17:
            totally_A = totally_A + 1
        else:
            totally_B = totally_B + 1

    if totally_A > totally_B:
        print(f"A has won {totally_A}")
    else:
        print(f"B has won {totally_B}")

elect()