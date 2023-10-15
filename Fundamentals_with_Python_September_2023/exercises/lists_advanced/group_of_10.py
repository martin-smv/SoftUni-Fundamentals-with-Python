list_with_numbers = [int(number) for number in input().split(", ")]

current_group = 10
while len(list_with_numbers) > 0:
    numbers_of_current_group = []

    for number in list_with_numbers:
        if number <= current_group:
            numbers_of_current_group.append(number)
    remove_numbers = [list_with_numbers.remove(num) for num in numbers_of_current_group]

    print(f"Group of {current_group}'s: {numbers_of_current_group}")

    current_group += 10