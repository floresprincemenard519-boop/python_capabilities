# make an infinite loop
# get numbers
# add them to a list 
# if invalid stop the loop
# sort the list
# print the list
list = []

while True:
    try:
        numbers = float(input("Please input a number: "))
        list.append(numbers)
    except ValueError:
        for num in sorted(list):
            print(num, end=" ")
        break