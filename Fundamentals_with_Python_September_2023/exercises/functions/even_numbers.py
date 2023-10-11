def is_even(number):
    if number % 2 == 0:
        return True
    return False


list_with_numbers = input().split()
list_with_numbers = [int(i) for i in list_with_numbers]

list_with_even_numbers = list(filter(is_even, list_with_numbers))
print(list_with_even_numbers)