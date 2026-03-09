string = "ABCDEFG HI! EHHEHE"
second_string = "AbCdEfG Hi! HeHeHe"
lower_string = ""

# how lower() works
print(string.lower())

# how lower() works without lower() method
for char in second_string:
    if char.isupper():
        lower_string += char.swapcase()
    else:
        lower_string += char

