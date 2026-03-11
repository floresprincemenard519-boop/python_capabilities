# get string
# check if length of string is lower than that of the inputed in rjust
# if so then add spaces or -

string = "I should be 50 characters long, but I'm not."
rjust_parameter = 50

if len(string) != rjust_parameter:
    print('-' * (rjust_parameter - len(string)) + string)
else:
    print(string)