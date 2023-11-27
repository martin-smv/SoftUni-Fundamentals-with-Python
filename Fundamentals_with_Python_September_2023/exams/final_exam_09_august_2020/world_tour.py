def add_stop(index, string, stops):
    if 0 <= index <= len(stops):
        stops = stops[:index] + string + stops[index:]
    print(stops)

    return stops


def remove_stop(start_index, end_index, stops):
    if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
        stops = stops[:start_index] + stops[end_index + 1:]
    print(stops)

    return stops


def switch(old_string, new_string, stops):
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    print(stops)

    return stops


stops = input()

command = input()
while command != "Travel":
    command = command.split(":")

    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        stops = add_stop(index, string, stops)

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        stops = remove_stop(start_index, end_index, stops)

    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        stops = switch(old_string, new_string, stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")