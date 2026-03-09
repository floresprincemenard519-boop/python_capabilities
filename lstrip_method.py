string = "   What a beautiful world! Helloooooo!"
spaceless_string = ""
non_space_detected = False

# how lstrip() works
print(string.lstrip())

# same functionality without using lstrip()
for char in string:
    if char != " " or non_space_detected:
        spaceless_string += char
        non_space_detected = True

print(spaceless_string)