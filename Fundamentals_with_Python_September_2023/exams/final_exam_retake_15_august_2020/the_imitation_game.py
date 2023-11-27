def move(n, text):
    text = text[n:] + text[:n]
    return text


def insert(i, v, text):
    text = text[:i] + v + text[i:]
    return text


def change(substr, replace_str, text):
    text = text.replace(substr, replace_str)
    return text


message = input()

command = input()
while command != "Decode":
    command = command.split("|")

    if command[0] == "Move":
        number = int(command[1])
        message = move(number, message)

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        message = insert(index, value, message)

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = change(substring, replacement, message)

    command = input()

print(f"The decrypted message is: {message}")