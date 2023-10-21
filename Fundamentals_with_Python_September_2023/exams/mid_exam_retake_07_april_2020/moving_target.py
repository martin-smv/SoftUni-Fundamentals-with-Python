def shoot_func(targets, index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def add_func(targets, index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike_func(targets, index, radius):
    if index + radius < len(targets) and index - radius >= 0:
        start_index = index - radius
        end_index = index + radius
        for i in range(start_index, end_index + 1):
            targets.pop(start_index)

    else:
        print("Strike missed!")


targets = [int(s) for s in input().split()]

while True:
    command = input().split()

    current_command = command[0]
    if current_command == "End":
        targets = [str(s) for s in targets]
        print("|".join(targets))
        break

    elif current_command == "Shoot":
        index, power = int(command[1]), int(command[2])
        shoot_func(targets, index, power)

    elif current_command == "Add":
        index, value = int(command[1]), int(command[2])
        add_func(targets, index, value)

    elif current_command == "Strike":
        index, radius = int(command[1]), int(command[2])
        strike_func(targets, index, radius)
