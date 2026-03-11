# get the input for the name 
# remove spaces from the beginning
# print result

fullname = input("Please input your full name.\n")
fullname = "     " + fullname
print(fullname)
print(fullname.lstrip(" "))
