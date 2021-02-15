# 17.​ Write a Python program to multiplies all the items in a list.


def multiply():
    list1 = [int(item) for item in (input("Enter the numbers in a comma separated sequence").split(","))]
    print(list1)

    product = 1
    for num in list1:
        product *= num
    return product


print("Product = ", multiply())
