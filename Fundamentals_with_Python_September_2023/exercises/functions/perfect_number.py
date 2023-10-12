def perfect_number(some_number: int):
    is_the_number_perfect = False
    sum_of_divisors = 0
    for current_number in range(1, some_number + 1):
        if some_number % current_number == 0:
            sum_of_divisors += current_number
    if sum_of_divisors - some_number == some_number:
        is_the_number_perfect = True
    return is_the_number_perfect


number = int(input())
is_perfect = perfect_number(number)

if is_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")