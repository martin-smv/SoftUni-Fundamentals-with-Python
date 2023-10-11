def return_all_characters_in_between(first, second):
    number_from_first = ord(first)
    number_from_second = ord(second)
    string_with_characters = ""

    for current_character in range(number_from_first + 1, number_from_second):
        string_with_characters += (chr(current_character)) + " "

    return string_with_characters


first_character = input()
second_character = input()
print(return_all_characters_in_between(first_character, second_character))