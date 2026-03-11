# get a string
# check each letter
# if letter is not lower
# print False

string = "The islower() of this string should return true."
isupper = True

for char in string:
    if char.isupper():
        isupper = False

print(isupper)