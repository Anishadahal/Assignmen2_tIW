# 20.​ Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def string_count():
    counter = 0
    list_string = [str(item) for item in (input("Enter the strings in comma separated sequence\n").split(","))]
    print(list_string)
    for string in list_string:
        if len(string) > 2 and string[0] == string[-1]:
            counter += 1
    return counter


count = string_count()
print(count)