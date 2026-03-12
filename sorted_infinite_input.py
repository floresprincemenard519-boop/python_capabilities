# make infinite input
# get numbers
# store number in list
# sort the list 
# print the list
all_numbers = []

while True:
    try:
        numbers = float(input("Please input a number: "))
        all_numbers.append(numbers)

    except ValueError:
        all_numbers.sort()

        for item in all_numbers:
            print(item, end=' ')

        break