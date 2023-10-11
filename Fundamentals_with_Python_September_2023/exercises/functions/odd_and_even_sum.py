def odd_and_even_sums(number: str):
    sum_of_even = 0
    sum_of_odd = 0

    for current_number in number:
        if int(current_number) % 2 == 0:
            sum_of_even += int(current_number)
        else:
            sum_of_odd += int(current_number)

    return sum_of_odd, sum_of_even


some_number = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sums(some_number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")