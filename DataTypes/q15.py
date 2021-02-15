# 15.​ Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_string_middle(outer, inner):
    mid = int(len(outer)/2)
    # print(outer)
    # print(outer[:mid])
    output = outer[:mid]+inner+outer[mid:]
    return output


input_outer = input("Enter the outer string\n")
input_inner = input("Enter the inner string\n")
result = insert_string_middle(input_outer, input_inner)
print(result)
