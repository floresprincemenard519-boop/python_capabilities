string = "i am a title of a book"
title_string = ""
# how title() method works
# print(string.title())

# how title() method works with title() method
for char in string:
    if string[string.index(char)-1] == " " or string.index(char) == 0:
        title_string += char.upper()
    elif string[string.index(char)-1].islower() == True:
        title_string += char.upper()


print(title_string)

# check each letter
# check if that letter is the beginning of the word
# change to cappital if it is the beginning of the word
# print all the letters together