# get 10 numbers
# add them to list 
# if is in the list remember them
# print them 

list = []
duplicated_numbers = set()

for num in range(10):
    numbers = float(input("Please input a number: "))
    if numbers in list:
        duplicated_numbers.add(numbers)
    else: 
        list.append(numbers)

for num in duplicated_numbers:
    print(num, end=' ')