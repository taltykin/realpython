try:
    user = int(input("Enter a number: "))
    print(user)
except ValueError:
    print("Not A Number!")