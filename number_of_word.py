word_counter = 0
statement = input("Please input a full statement: ")

for index, char in enumerate(statement):
    if index == 0 or statement[index-1] == ' ':
        word_counter += 1
        
print(word_counter)