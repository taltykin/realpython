n = int(input("Please, enter positive integer: "))
# if (12 % n) == 0:
#     print(f"{n} is a factor of 12")
# else:
#     print(f"{n} is NOT a factor of 12")

for item in range(1, n + 1):
    if n % item == 0:
        print(f"{item} is a factor of {n}")