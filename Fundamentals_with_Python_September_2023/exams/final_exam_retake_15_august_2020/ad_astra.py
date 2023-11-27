import re

some_string = input()
pattern = r"([#\|])([\w\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.finditer(pattern, some_string)

matches_list = []
total_calories = 0
for match in matches:
    matches_list.append([match.group(2), match.group(3), match.group(4)])
    total_calories += int(match.group(4))

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for match in matches_list:
    item_name = match[0]
    date = match[1]
    calories = match[2]
    print(f"Item: {item_name}, Best before: {date}, Nutrition: {calories}")