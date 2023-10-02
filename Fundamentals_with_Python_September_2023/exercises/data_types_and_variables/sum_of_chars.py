number_of_lines = int(input())
sum_of_characters = 0
for current_line in range(number_of_lines):
    character = input()
    number_of_character = ord(character)
    sum_of_characters += number_of_character
print(f"The sum equals: {sum_of_characters}")