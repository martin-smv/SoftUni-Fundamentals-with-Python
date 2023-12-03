import re

number_of_strings = int(input())
pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"
for i in range(number_of_strings):
    some_string = input()
    match = re.match(pattern, some_string)
    if match:
        command = match.group(1)
        string = match.group(2)
        translated_string = [str(ord(i)) for i in string]
        print(f"{command}: {' '.join(translated_string)}")
    else:
        print("The message is invalid")
