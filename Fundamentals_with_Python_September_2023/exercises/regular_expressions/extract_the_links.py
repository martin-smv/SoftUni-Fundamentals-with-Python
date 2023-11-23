import re

pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
text = input()
while text:
    matches = re.search(pattern, text)
    if matches:
        valid_url = matches.group(1)
        print(valid_url)
    text = input()
