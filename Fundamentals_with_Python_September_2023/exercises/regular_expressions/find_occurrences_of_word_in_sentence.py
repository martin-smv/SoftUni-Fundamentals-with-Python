import re

text = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"
matches = re.findall(pattern, text)

print(len(matches))