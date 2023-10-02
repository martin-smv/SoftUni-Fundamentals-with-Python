number_of_lines = int(input())
positive_numbers = []
negative_numbers = []
for current_number in range(number_of_lines):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
print(positive_numbers)
print(negative_numbers)
positive_numbers = len(positive_numbers)
negative_numbers = sum((negative_numbers))
print(f"Count of positives: {positive_numbers}")
print(f"Sum of negatives: {negative_numbers}")