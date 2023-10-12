def calculate_factorial(first, second: int):
    result = 0
    first_sum_of_numbers = 1
    second_sum_of_numbers = 1

    for number in range(1, first + 1):
        first_sum_of_numbers = first_sum_of_numbers * number

    for number in range(1, second + 1):
        second_sum_of_numbers = second_sum_of_numbers * number

    result = first_sum_of_numbers / second_sum_of_numbers
    return result


first_number = int(input())
second_number = int(input())
final_result = calculate_factorial(first_number, second_number)
print(f"{final_result:.2f}")