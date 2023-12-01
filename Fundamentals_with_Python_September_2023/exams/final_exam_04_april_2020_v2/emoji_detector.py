import re


def multiply_digits(some_text):
    sum_of_all_numbers = 1
    pattern = r"\d"
    matches = re.findall(pattern, some_text)
    for match in matches:
        sum_of_all_numbers = sum_of_all_numbers * int(match)

    return sum_of_all_numbers


def find_emojis(some_text):
    pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
    matches = re.finditer(pattern, some_text)

    return matches


def emojis_to_numbers():
    emojis_list = find_emojis(text)
    numbers_of_emojis = {}

    for emoji in emojis_list:
        sum_of_emoji = 0
        for char in emoji.group(2):
            number = ord(char)
            sum_of_emoji += number
        numbers_of_emojis[emoji] = sum_of_emoji

    return numbers_of_emojis


text = input()

cool_threshold = multiply_digits(text)
number_of_emojis = len(emojis_to_numbers())
print(f"Cool threshold: {cool_threshold}")
print(f"{number_of_emojis} emojis found in the text. The cool ones are:")
for current_emoji, coolness in emojis_to_numbers().items():
    if coolness >= cool_threshold:
        print(current_emoji.group())
