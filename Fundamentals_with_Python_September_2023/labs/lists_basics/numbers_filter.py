number_of_lines = int(input())
list_of_numbers = []
filtered_list = []
for i in range(number_of_lines):
    number = int(input())
    list_of_numbers.append(number)
command = input()
if command == "even":
    for current_number in list_of_numbers:
        if current_number % 2 == 0:
            filtered_list.append(current_number)
elif command == "odd":
    for current_number in list_of_numbers:
        if current_number % 2 != 0:
            filtered_list.append(current_number)
elif command == "negative":
    for current_number in list_of_numbers:
        if current_number < 0:
            filtered_list.append(current_number)
elif command == "positive":
    for current_number in list_of_numbers:
        if current_number >= 0:
            filtered_list.append(current_number)
print(filtered_list)