elements = input().split()

moves_counter = 0
command = input()
while command != "end":
    current_indexes = command.split()
    first_index = int(current_indexes[0])
    second_index = int(current_indexes[1])
    moves_counter += 1

    if first_index == second_index \
            or 0 > first_index or first_index > len(elements) - 1 \
            or 0 > second_index or second_index > len(elements) - 1:
        midpoint = len(elements) // 2
        [elements.insert(midpoint, f"-{moves_counter}a") for i in range(2)]
        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        elements = [i for i in elements if i != elements[first_index]]
    else:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves_counter} turns!")
        break

    command = input()

if len(elements) > 0:
    print(f"Sorry you lose :(\n"
          f"{' '.join(elements)}")
