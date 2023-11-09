string = input()

digits = ""
letters = ""
characters = ""
for element in string:
    if element.isdigit():
        digits += element
    elif element.isalpha():
        letters += element
    else:
        characters += element

print(digits)
print(letters)
print(characters)