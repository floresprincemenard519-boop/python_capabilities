# get a string
# check each letter for the parameter
# give the index/range of the parameter

string = "The first location of 'i' is 6."
index_parameter = 'i'

for i in range(len(string)):
    if string[i-1] == 'i':
        print(i)
        break
