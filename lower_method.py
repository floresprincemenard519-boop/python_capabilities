string = "ABCDEFG HI! EHHEHE"

lower_string = ""
# how lower() works
print(string.lower())

# how lower() works without lower() method
# can't do without lower() method cause dont know how convert that to numbers then to acii
#  but i discovered i can use swapcase so im gonna use that 
for char in string:
    if char.isupper():
        lower_string += char.swapcase()
    else:
        lower_string += char

