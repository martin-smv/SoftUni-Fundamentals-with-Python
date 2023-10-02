lines = int(input())
some_word = input()
strings = []
for current_line in range(lines):
    text = input()
    strings.append(text)
print(strings)
for index in range(len(strings) - 1, - 1, - 1):
    element = strings[index]
    if some_word not in element:
        strings.remove(element)
print(strings)