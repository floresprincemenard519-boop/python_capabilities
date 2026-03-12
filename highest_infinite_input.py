# make an infinite loop to get numbers
# store the numbers in list
# get the highest 
# print the highest 
list = []

while True:
    try:
        numbers = float(input("Please input a number: "))
        list.append(numbers)
    except ValueError:
        print(max(list))
        break