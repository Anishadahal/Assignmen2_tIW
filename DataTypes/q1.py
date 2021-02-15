# 1. Write a Python program to count the number of characters (character frequency) in a string. Sample String :
# google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

#
# def count_characters():
#     count = 1
#     string = "google.com"
#     char_freq = {}
#
#     if len(string) > 0:
#         for i in string:
#             # print("INside for")
#             if i in char_freq:
#                 char_freq[i] += count
#             else:
#                 char_freq[i] = count
#     print("RESULT: " + str(char_freq))
#
#
# count_characters()

count = 1
string = "google.com"
char_freq = {}

if len(string) > 0:
    for i in string:
        # print("INside for")
        if i in char_freq:
            char_freq[i] += count
        else:
            char_freq[i] = count
print("RESULT: " + str(char_freq))
