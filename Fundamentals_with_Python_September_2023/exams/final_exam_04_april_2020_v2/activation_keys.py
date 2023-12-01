activation_key = input()

command = input()
while command != "Generate":
    command = command.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        sec_command = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = activation_key[start_index:end_index]
        if sec_command == "Upper":
            substring = substring.upper()
        elif sec_command == "Lower":
            substring = substring.lower()
        activation_key = activation_key[:start_index] + substring + activation_key[end_index:]
        print(activation_key)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")