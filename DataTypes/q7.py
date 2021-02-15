# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.


def find_longest_word(text):
    longest = 0
    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words
    return longest_word


input_string = input("Please input a list of words to evaluate: ")
longest_word = find_longest_word(input_string)
length = len(longest_word)
print("The longest word is", longest_word, "with length", length)
