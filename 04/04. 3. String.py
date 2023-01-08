string = ["     Animals", "Badger       ", "  Honey Bee   ", "   Honey Badger   "]

out = []

i = 0
while i < len(string):
    out.append(string[i].lower().strip())  # switch to upper() if need CAPITAL letters.
    i += 1

print(out)