characters = input().lower().split()

char_dictionary = {}
for char in characters:
    if char not in char_dictionary:
        char_dictionary[char] = 1
    else:
        char_dictionary[char] += 1

result = []
for character, count in char_dictionary.items():
    if count % 2 != 0:
        result.append(character)

print(" ".join(result))