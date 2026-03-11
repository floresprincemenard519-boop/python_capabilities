# get the fullname
# check each letters and compare if it has space before it if it does it means its a start of a word
# if a start make capital
# print all the letters

fullname = input("Please input your fullname: ")

for index, char in enumerate(fullname):
    if index == 0 or fullname[index - 1] == ' ':
        print(char.upper(), end="")
    elif char == ' ':
        print('', end='')
    else:
        print(char, end="")