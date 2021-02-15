# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def change_occurrence():
    text = input("Enter string \n")
    result = text[0]+text.replace(text[0], "$")[1:]
    print(result)


change_occurrence()
