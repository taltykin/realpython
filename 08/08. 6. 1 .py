# try:
#     user = int(input("Enter a number: "))
#     print(user)
# except ValueError:
#     print("Not A Number!")

try:
    string = str(input("Введите строку: "))
    number = int(input("Введите число: "))
    print(string[number])
except ValueError:
    print("Введите правильное значение!")