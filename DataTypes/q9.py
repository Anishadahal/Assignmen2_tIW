# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def exchange_characters():
    text = input("Enter a string\n")
    a = text[0]
    print(a)
    b = text[-1]
    result = b + text[1:-1] + a
    print(result)


exchange_characters()