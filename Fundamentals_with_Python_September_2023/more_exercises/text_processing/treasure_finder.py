def find_type(some_text):
    for index in range(len(some_text)):
        if some_text[index] == "&":
            next_enclosing_element = some_text.find("&", index + 1)
            return some_text[index + 1: next_enclosing_element]


def find_coordinates(some_text):
    for index in range(len(some_text)):
        if some_text[index] == "<":
            next_enclosing_element = some_text.find(">", index + 1)
            return some_text[index + 1: next_enclosing_element]


keys = [int(s) for s in input().split()]

while True:
    text = input()
    if text == "find":
        break

    secret_message = ""
    index = 0
    for char in text:
        if index == len(keys):
            index = 0

        new_char = chr(ord(char) - keys[index])
        secret_message += new_char
        index += 1

    treasure_type = find_type(secret_message)
    coordinates = find_coordinates(secret_message)

    print(f"Found {treasure_type} at {coordinates}")