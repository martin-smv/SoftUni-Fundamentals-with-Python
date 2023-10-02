start_index = int(input())
final_index = int(input())
for number in range(start_index, final_index + 1):
    current_character = chr(number)
    if number == final_index:
        print(current_character)
    else:
        print(current_character, end=" ")