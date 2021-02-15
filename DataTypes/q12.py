# 12. ​ Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.

def change_cases():
    text = input("Enter input string\n")
    ucase_text = text.upper()
    lcase_text = text.lower()
    print("Upper case resut:" + ucase_text)
    print("Lower case resut:" + lcase_text)


change_cases()
