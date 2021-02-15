# 11. ​ Write a Python program to count the occurrences of each word in a given
# sentence.

def count_word_occurrence():
    count = dict()
    data = input("Enter a sentence \n")
    word_list = data.split(" ")
    # print(word_list)

    for i in word_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)


count_word_occurrence()