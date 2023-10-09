list_with_numbers = input().split()

absolute_values = []
for current_number in list_with_numbers:
    absolute_values.append(abs(float(current_number)))
print(absolute_values)