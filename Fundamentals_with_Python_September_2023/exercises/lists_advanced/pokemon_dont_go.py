numbers = [int(s) for s in input().split()]

sum_of_removed_numbers = 0
while numbers:
    index = int(input())

    if index < 0:
        index = 0
        numbers.insert(0, numbers[-1])
    elif index > len(numbers) - 1:
        index = len(numbers) - 1
        numbers.insert(-1, numbers[0])

    popped_element = numbers.pop(index)
    sum_of_removed_numbers += popped_element
    for current_index in range(len(numbers)):
        if numbers[current_index] <= popped_element:
            numbers[current_index] += popped_element
        else:
            numbers[current_index] -= popped_element

print(sum_of_removed_numbers)