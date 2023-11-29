def insert_space(index, text):
    first_part = text[:index]
    second_part = text[index:]
    text = first_part + " " + second_part
    print(text)

    return text


def reverse(substring, text):
    if substring in text:
        reversed_substring = substring[::-1]
        text = text.replace(substring, "", 1)
        text = text + reversed_substring
        print(text)
    else:
        print("error")

    return text


def change_all(substring, replacement, text):
    text = text.replace(substring, replacement)
    print(text)

    return text


concealed_message = input()

command = input()
while command != "Reveal":
    command = command.split(":|:")

    if command[0] == "InsertSpace":
        index = int(command[1])
        concealed_message = insert_space(index, concealed_message)

    elif command[0] == "Reverse":
        string = command[1]
        concealed_message = reverse(string, concealed_message)

    elif command[0] == "ChangeAll":
        string = command[1]
        replacement = command[2]
        concealed_message = change_all(string, replacement, concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")