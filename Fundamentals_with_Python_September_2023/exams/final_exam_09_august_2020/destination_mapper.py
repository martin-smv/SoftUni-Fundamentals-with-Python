import re

some_string = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, some_string)

destinations = []
travel_points = 0
for match in matches:
    destination = match[1]
    points = len(destination)
    travel_points += points
    destinations.append(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")