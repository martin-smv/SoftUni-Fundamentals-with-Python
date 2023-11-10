from string import ascii_lowercase


def first_letter(char, num):
    num_of_first_char = alphabet.index(char.lower()) + 1
    if char.isupper():
        result = num / num_of_first_char
    elif char.islower():
        result = num * num_of_first_char

    return result


def second_letter(char):
    num_of_second_char = alphabet.index(char.lower()) + 1
    if char.isupper():
        result = first_letter(first_char, number) - num_of_second_char
    elif char.islower():
        result = first_letter(first_char, number) + num_of_second_char

    return result


alphabet = list(ascii_lowercase)
some_string = input().split()

total_sum = 0
for string in some_string:
    number = int(string[1: -1])
    first_char = string[0]
    second_char = string[-1:]
    total_sum += second_letter(second_char)

print(f"{total_sum:.2f}")