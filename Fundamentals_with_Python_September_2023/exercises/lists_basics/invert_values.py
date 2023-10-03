list_of_numbers = input().split()
reversed_numbers = []
for number in list_of_numbers:
    current_number = int(number)
    if current_number >= 0:
        reversed_numbers.append(-abs(current_number))
    elif current_number < 0:
        reversed_numbers.append(abs(current_number))
print(reversed_numbers)