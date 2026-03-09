string = "i am a title of a book"
title_string = ""

# how title() method works
print(string.title())

# how title() method works with title() method
for index, char in enumerate(string):
    if index == 0 or string[index-1] == " ":
        title_string += char.upper()
    elif string[index-1] == char.isupper():
        title_string += char.lower()
    else:
        title_string += char

print(title_string)
