large_string = "I SHOULD BE SMALL"
small_string = "i should be large"

# how swapcase() works
print(large_string.swapcase())
print(small_string.swapcase())

# how swapcase() works without using swapcase() method
def swapcase(string):
    if string.isupper():
        string = string.lower()
    elif string.islower():
        string = string.upper()
    print(string)

swapcase(large_string)
swapcase(small_string)