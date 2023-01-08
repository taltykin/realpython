str1 = "Becomes"
str2 = "becomes"
str3 = "BEAR"
str4 = " bEautiful"

print(str1.lower().startswith("be"))
print(str2.startswith("be"))
print(str3.lower().startswith("be"))
print(str4.lstrip().lower().startswith("be"))