string = "I should be in          the center."

# how center() works
print(string.center(50,"-"))

# how center() works without center() method
if len(string) != 50:
    padding = (50 - len(string)) //2
    print('-' * padding + string + '-' * padding)
else:
    print(string)
