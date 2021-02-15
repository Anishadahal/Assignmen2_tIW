# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

string = input("Enter a sentence\n")
index_not = string.find("not")
# print(index_not)
index_poor = string.find("poor")

if index_poor > index_not and index_not > 0 and index_poor > 0:
    string = string.replace(string[index_not:(index_poor+4)], "good")
    print(string)
else:
    print(string)





