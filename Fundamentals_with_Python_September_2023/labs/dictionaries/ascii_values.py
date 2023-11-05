characters = input().split(", ")

dictionary_with_chars = {}
for char in characters:
    dictionary_with_chars[char] = ord(char)

print(dictionary_with_chars)