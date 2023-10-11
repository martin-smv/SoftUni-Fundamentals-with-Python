def returns_smallest_number(a, b, c) -> int:
    return min(a, b, c)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = returns_smallest_number(first_number, second_number, third_number)
print(smallest_number)