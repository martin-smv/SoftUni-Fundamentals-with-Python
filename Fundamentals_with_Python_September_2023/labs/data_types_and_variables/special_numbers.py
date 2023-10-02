number = int(input())
for current_number in range(1, number + 1):
    sum_of_digits = 0
    for digit in str(current_number):
        sum_of_digits += int(digit)
    is_number_special = False
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_number_special = True
    print(f"{current_number} -> {is_number_special}")