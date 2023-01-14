def convert_cel_to_far():

    inp = float(input("Please, enter tempurature in celcius degrees: "))

    convert = inp * 9 / 5 + 32

    return convert


def convert_far _to_cel():
    inp = float(input("Please, enter tempurature: "))
    convert = (inp - 32) * 5 / 9