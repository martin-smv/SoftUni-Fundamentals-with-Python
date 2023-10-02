command = input()
while command != "End":
    if command != "SoftUni":
        new_command = ""
        for character in command:
            new_command += character * 2
        print(new_command)
    command = input()