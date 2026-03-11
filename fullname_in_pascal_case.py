fullname = input("Please input your fullname: ")
fullname = fullname.title()

for char in fullname:
    if char == ' ':
        print('', end='')
    else:
        print(char, end="")