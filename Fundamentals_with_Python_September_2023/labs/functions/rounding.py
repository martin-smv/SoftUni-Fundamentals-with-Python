list_with_numbers = input().split()

rounded_numbers = []
for current_number in list_with_numbers:
    rounded_numbers.append(round(float(current_number)))
print(rounded_numbers)