first_input = int(input("Inter first number:"))
second_input = int(input("Inter second number:"))

multiplication = first_input * second_input

out = "The product of {x} and {y} is {z}".format(x = first_input, y = second_input, z = multiplication)

print(out)