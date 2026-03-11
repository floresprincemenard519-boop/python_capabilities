# get string
# check if a character is in beginning of the string
# return False or True
string = "This string should return True with startswith()."
beginning = "This"

if beginning in string[:len(beginning)]:
    print(True)
else:
    print(False)