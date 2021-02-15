# 16.​ Write a Python program to sum all the items in a list.


def sum_list():
    list1 = [int(item) for item in input("Enter the list items : ").split(",")]
    sum_list = 0
    for numbers in list1:
        print(list1)
        sum_list += numbers
    return sum_list


result = sum_list()
print(result)
