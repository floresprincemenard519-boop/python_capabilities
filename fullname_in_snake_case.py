fullname = input("Please input your fullname in improper casing: ")
fullname = fullname.lower()

for char in fullname:
    if char == ' ':
        print('_', end="")
    else:
        print(char, end="")