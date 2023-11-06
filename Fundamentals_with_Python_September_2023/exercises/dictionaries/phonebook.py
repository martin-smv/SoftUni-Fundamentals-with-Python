def show_details():
    if searched_name in phonebook.keys():
        return f"{searched_name} -> {phonebook[searched_name]}"
    return f"Contact {searched_name} does not exist."


phonebook = {}

while True:
    command = input()
    if command.isdigit():
        number = int(command)
        break

    name, phone_number = command.split("-")
    phonebook[name] = phone_number

for n in range(number):
    searched_name = input()
    print(show_details())