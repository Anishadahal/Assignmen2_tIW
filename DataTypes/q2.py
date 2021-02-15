# 2. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.
# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'Py'
# Expected Result : 'PyPy'
# Sample String : ' w'
# Expected Result : Empty String


def sub_string():
    list1 = {}
    text = input("Enter a string \n")
    if len(text) > 0:
        # try:
        #     for i in text:
        #         list1 = text[0] + text[1] + text[-2] + text[-1]
        #     print(list1)
        # except:
        #     print("Empty String")

        if len(text) < 2:
            print("Empty string.")
        else:
            for i in text:
                list1 = text[0] + text[1] + text[-2] + text[-1]
            print(list1)


sub_string()
