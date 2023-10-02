command = input()
while command != "Welcome!":
    name_length = len(command)
    if command == "Voldemort":
        break
    if name_length < 5:
        print(f"{command} goes to Gryffindor.")
    elif name_length == 5:
        print(f"{command} goes to Slytherin.")
    elif name_length == 6:
        print(f"{command} goes to Ravenclaw.")
    elif name_length > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()

if command == "Voldemort":
    print(f"You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")