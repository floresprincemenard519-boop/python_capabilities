first_number = float(input("Give me a number: "))
second_number = float(input("Give me another: "))
third_number = float(input("Another: "))
list = []

print(first_number + second_number + third_number)

for number in range(5):
    number = float(input("Give me a number: "))
    list.append(number)

print(sum(list))