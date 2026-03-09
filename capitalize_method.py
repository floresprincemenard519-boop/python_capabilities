string = "i should have a capital letter at the beginning."

# how capitalize() works
print(string.capitalize())

# how capitalize() works without capitalize() method
for char in string[0]:
    if char.islower():
        char = char.upper()
        print(char)
