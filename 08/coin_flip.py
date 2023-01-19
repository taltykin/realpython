import random

# def coin_flip():
#     if random.randint(0, 1) == 0:
#         return "heads"
#     else:
#         return "tails"

# heads = 0
# tails = 0

# for n in range(10000):
#     if coin_flip() == "heads":
#         heads = heads + n
#     else:
#         tails = tails + n

# print(f"heads are {heads}, tails are {tails}")


def coin_flip():
    first_try = random.randint(0, 1)

    attemption_counter = 1

    while first_try == random.randint(0, 1):
        attemption_counter = attemption_counter + 1

    attemption_counter = attemption_counter + 1
    return attemption_counter

def attemption(num_trials):
    total = 0
    for n in range(num_trials):
        total = total + coin_flip()
    
    ratio = total / num_trials

    print(ratio)

attemption(10000)