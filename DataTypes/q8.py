# 8. Write a Python program to remove the nth index character from a nonempty
# string.


def remove_character():
    text = input("Enter string\n")
    index = input("Which index ddo you want to remove?")
    i = int(index)

    first_part = text[:i]
    second_part = text[i+1:]
    result = first_part + second_part
    print(result)


remove_character()
