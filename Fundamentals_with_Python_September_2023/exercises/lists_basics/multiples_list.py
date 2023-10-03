factor_number = int(input())
count_number = int(input())
list_of_numbers = []
for number in range(1, count_number + 1):
    list_of_numbers.append(factor_number * number)
print(list_of_numbers)