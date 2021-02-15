# 18.​ Write a Python program to get the largest number from a list.

def largest_number():
    list1 = [int(item) for item in (input("Enter the numbers in a comma separated sequence\n").split(","))]
    print(list1)

    largest = 0
    for num in list1:
        if num > largest:
            largest = num
    return largest


print("Largest Number = ", largest_number())