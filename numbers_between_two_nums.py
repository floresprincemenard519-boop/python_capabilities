first_number = int(input("Please input a number: "))
second_number = int(input("please input another number: "))

if first_number > second_number + 1:
    while first_number != second_number:
        first_number -= 1
        print(first_number, end=" ")
elif second_number > first_number:
    while second_number!= first_number + 1:
        second_number -= 1
        print(second_number, end=" ")
else:
    print("The numbers are equal.")