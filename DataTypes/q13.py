# 13. ​ Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically)

def sort_words():
    items = input("Input comma separated sequence of words \n")
    words = items.split(",")
    result = "\n".join(sorted(list(set(words))))
    print("Unique and sorted: \n")
    print(result)


sort_words()
