# 19.​ Write a Python program to get the smallest number from a list.
def smallest_number():
    list1 = [int(item) for item in (input("Enter the numbers in a comma separated sequence\n").split(","))]
    print(list1)
    return min(list1)

    # smallest = 0
    # for num in list1:
    #     if num < smallest:
    #         smallest = num
    # return smallest


print("Smallest Number = ", smallest_number())
