password = input()
new_password = ""

command = input()
while command != "Done":
    command = command.split()

    if command[0] == "TakeOdd":
        for index in range(len(password)):
            if index % 2 != 0:
                new_password += password[index]
        password = new_password
        new_password = ""
        print(password)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        first_part = password[:index]
        second_part = password[index + length:]
        password = first_part + second_part
        print(password)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")