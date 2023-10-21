def swap_func(array, first_index, second_index):
    array[first_index], array[second_index] = array[second_index], array[first_index]


def multiply_func(array, first_index, second_index):
    result = array[first_index] * array[second_index]
    array[first_index] = result


def decrease_func(array):
    for i in range(len(array)):
        array[i] = array[i] - 1


array = [int(s) for s in input().split()]
while True:
    command = input().split()

    current_command = command[0]

    if current_command == "end":
        break

    elif current_command == "swap":
        first, second = int(command[1]), int(command[2])
        swap_func(array, first, second)

    elif current_command == "multiply":
        first, second = int(command[1]), int(command[2])
        multiply_func(array, first, second)

    elif current_command == "decrease":
        decrease_func(array)

array = [str(s) for s in array]
print(", ".join(array))