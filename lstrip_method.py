# lstrip() example function
string = "   What a beautiful world! Helloooooo!"
# print(string.lstrip())
spaceless_string = ""
# remove spaces without using lstrip()

# check if the characters in string is space or not
for char in string:
    if char != " ":
        spaceless_string += char
# if character is space then remove it from the string

# if encountered a non space dont remove spaces further 

print(spaceless_string)