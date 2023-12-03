password = input()

command = input()
while command != "Complete":
    command = command.split()

    if command[0] == "Validation":
        upper_validation = 0
        lower_validation = 0
        digit_validation = 0

        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        for character in password:
            if not character.isalpha() and not character.isdigit() and not character == "_":
                print("Password must consist only of letters, digits and _!")
                break

            if character.isupper() and upper_validation < 1:
                upper_validation += 1
            elif character.islower() and lower_validation < 1:
                lower_validation += 1
            elif character.isdigit() and digit_validation < 1:
                digit_validation += 1

        if upper_validation < 1:
            print("Password must consist at least one uppercase letter!")

        if lower_validation < 1:
            print("Password must consist at least one lowercase letter!")

        if digit_validation < 1:
            print("Password must consist at least one digit!")

    elif command[0] + " " + command[1] == "Make Upper":
        index = int(command[2])
        password = password[:index] + password[index].upper() + password[index + 1:]
        print(password)

    elif command[0] + " " + command[1] == "Make Lower":
        index = int(command[2])
        password = password[:index] + password[index].lower() + password[index + 1:]
        print(password)

    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        if index < len(password):
            password = password[:index] + char + password[index:]
            print(password)

    elif command[0] == "Replace":
        char = command[1]
        value = int(command[2])
        if char in password:
            new_char = chr(ord(char) + value)
            password = password.replace(char, new_char)
            print(password)

    command = input()
