data_type = input()
command = input()

if data_type == "int":
    number = int(command)
    result = number * 2

elif data_type == "real":
    number = float(command)
    result = f"{number * 1.5:.2f}"

elif data_type == "string":
    string = command.split()
    string.insert(0, "$")
    string.insert(len(string), "$")
    result = "".join(string)

print(result)