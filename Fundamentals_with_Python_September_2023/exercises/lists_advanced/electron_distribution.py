number_of_electrons = int(input())
shells = []

shell = 1
while number_of_electrons > 0:
    electrons_in_current_shell = 2 * shell ** 2

    if number_of_electrons >= electrons_in_current_shell:
        shells.append(electrons_in_current_shell)
        number_of_electrons -= electrons_in_current_shell
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
    shell += 1

print(shells)