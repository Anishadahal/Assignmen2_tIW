# 14. Write a Python function to create the HTML string with tags around the
# word(s).

def create_html_tags(string, tag):
    output = "<"+tag+">"+string+"</"+tag+">"
    return output


input_string = input("enter the string\n")
input_tag = input("Enter the tag\n")
result = create_html_tags(input_string, input_tag)
print(result)