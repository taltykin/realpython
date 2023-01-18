from random import randint

def flip_coin():
    if randint(0, 1) == 0:
        print("0")
    else:
        print("1")

flip_coin()


# def roll():
#     """Return random integer between 1 and 6"""
#     return randint(1, 6)