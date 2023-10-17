def merge_strings():
    start_index = int(command[1])
    end_index = int(command[2])

    if start_index < 0:
        start_index = 0
    if end_index > len(data) - 1:
        end_index = len(data) - 1

    merge = "".join(data[start_index:end_index + 1])

    data[start_index:end_index + 1] = [merge]

    return


def divide_strings():
    index = int(command[1])
    count = int(command[2])

    string = data[index]
    partition_length = len(string) // count

    new_string = []
    for current_index in range(count):
        if current_index != count - 1:
            new_string.append(string[current_index * partition_length: (current_index + 1) * partition_length])
        else:
            new_string.append(string[current_index * partition_length:])

    data[index:index + 1] = new_string

    return


data = input().split()

while True:
    command = input().split()

    if command[0] == "3:1":
        break

    if command[0] == "merge":
        merge_strings()

    elif command[0] == "divide":
        divide_strings()

print(" ".join(data))