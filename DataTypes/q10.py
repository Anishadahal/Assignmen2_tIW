# 10. Write a Python program to remove the characters which have odd index
# values of a given string.


def remove_odd():
    result = ""
    text = input("Enter String\n")
    for i in range(len(text)):
        if i % 2 == 0:
            result = result + text[i]
    print(result)


remove_odd()
