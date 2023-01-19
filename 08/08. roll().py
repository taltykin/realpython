import random

def roll():
    return random.randint(1, 6)


reps = 10_000
avar = 0
counter = 0
for item in range(reps):
    counter = counter + roll()

avar = counter / reps

print(avar)

# def roll():
#     """Return random integer between 1 and 6"""
#     return randint(1, 6)