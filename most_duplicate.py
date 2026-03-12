# make infinite loop
# get numbers
# get the highest num of duplicates
# print the number not the count
list = {}
highest_number = None
highest_count = -1

while True:
    try:
        numbers = float(input("Please input a number: "))
        list[numbers] = list.get(numbers,0) + 1
    
    except ValueError:
        for number, count in list.items():
            if count > highest_count:
                highest_count = count
                highest_number = number
        print(highest_number)
        break

    