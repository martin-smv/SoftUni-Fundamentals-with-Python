first_word, second_word = input().split()

total_sum = 0

remaining_chars = ""
difference = 0
if len(first_word) > len(second_word):
    difference = len(second_word) - len(first_word)
    remaining_chars = first_word[difference:]
    first_word = first_word[:difference]

elif len(first_word) < len(second_word):
    difference = len(first_word) - len(second_word)
    remaining_chars = second_word[difference:]
    second_word = second_word[:difference]

for first_char, second_char in zip(first_word, second_word):
    total_sum += ord(first_char) * ord(second_char)

for char in remaining_chars:
    total_sum += ord(char)

print(total_sum)
