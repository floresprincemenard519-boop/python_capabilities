string = "i am a title of a book"

# how title() method works
print(string.title())

# how title() method works with title() method
for char in string:
    if string.index(char)-1 == ' ':
        print(char.upper(), end="")
    else:
        print(char, end="")

# check each letter
# check if that letter is the beginning of the word
# change to cappital if it is the beginning of the word
# print all the letters together