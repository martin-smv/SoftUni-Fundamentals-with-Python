sequence = [int(s) for s in input().split()]

command = input()
shots_counter = 0
while command != "End":
    index = int(command)

    if index < 0 or index > len(sequence) - 1:
        command = input()
        continue

    target = sequence[index]
    for current_index in range(len(sequence)):
        if sequence[current_index] > sequence[index] and sequence[current_index] >= 0:
            sequence[current_index] -= target

        else:
            if sequence[current_index] >= 0:
                sequence[current_index] += target

        sequence[index] = target

    sequence[index] = -1
    shots_counter += 1

    command = input()

sequence = [str(s) for s in sequence]
print(f'Shot targets: {shots_counter} -> {" ".join(sequence)}')