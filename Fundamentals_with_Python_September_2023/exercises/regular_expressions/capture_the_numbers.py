import re

text = input()
while text:
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    if matches:
        print(" ".join(matches), end=" ")
    text = input()