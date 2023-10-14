def index_of_even_number():
    list_with_indexes = [index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]

    return list_with_indexes


numbers = input().split(", ")
print(index_of_even_number())