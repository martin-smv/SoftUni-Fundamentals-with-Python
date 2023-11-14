def find_name(some_text, index):
    index_of_second_element = some_text.find("|", index)
    return some_text[index + 1: index_of_second_element]


def find_age(some_text, index):
    index_of_second_element = some_text.find("*", index)
    return some_text[index + 1: index_of_second_element]


number_of_lines = int(input())

for line in range(number_of_lines):
    text = input()
    for index in range(len(text)):
        if text[index] == "@":
            name = find_name(text, index)
        elif text[index] == "#":
            age = find_age(text, index)
    print(f"{name} is {age} years old.")
