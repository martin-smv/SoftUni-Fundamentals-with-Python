import re

mirrored_words = {}

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
matches = re.finditer(pattern, text)

number_of_pairs = len(re.findall(pattern,text))
for match in matches:
    first_word = match.group(2)
    second_word = match.group(3)
    if second_word[::-1] == first_word:
        mirrored_words[first_word] = second_word

if number_of_pairs:
    print(f"{number_of_pairs} word pairs found!")
else:
    print("No word pairs found!")

if mirrored_words:
    print("The mirror words are:")
    print(', '.join('{} <=> {}'.format(k, v) for k, v in mirrored_words.items()))
else:
    print("No mirror words!")