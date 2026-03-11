list = []

while True:
    try:
        numbers = float(input("Input a number please: "))
        list.append(numbers)
    except ValueError:
        print(min(list))
        break