def include(list_with_coffees, coffee):
    list_with_coffees.append(coffee)


def remove(list_with_coffees, first_or_last, n_coffees):
    if len(list_with_coffees) >= n_coffees:
        for i in range(n_coffees):
            if first_or_last == "first":
                list_with_coffees.pop(0)
            else:
                list_with_coffees.pop()


def prefer(list_with_coffees, first_index, second_index):
    if 0 <= first_index < len(list_with_coffees) and 0 <= second_index < len(list_with_coffees):
        list_with_coffees[first_index], list_with_coffees[second_index] = \
            list_with_coffees[second_index], list_with_coffees[first_index]


coffees = input().split()
number_of_commands = int(input())

for s in range(number_of_commands):
    command = input().split()
    current_command = command[0]

    if current_command == "Include":
        coffee_name = command[1]
        include(coffees, coffee_name)

    elif current_command == "Remove":
        first_or_last = command[1]
        number_of_coffees = int(command[2])
        remove(coffees, first_or_last, number_of_coffees)

    elif current_command == "Prefer":
        first_index = int(command[1])
        second_index = int(command[2])
        prefer(coffees, first_index, second_index)

    elif current_command == "Reverse":
        coffees = coffees[::-1]

print("Coffees:")
print(" ".join(coffees))