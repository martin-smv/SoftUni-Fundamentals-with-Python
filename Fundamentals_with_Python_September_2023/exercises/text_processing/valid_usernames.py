usernames = input().split(", ")

for name in usernames:
    string = ""
    if 3 < len(name) < 16:
        for char in name:
            if char.isalpha() or char.isdigit() or char == "-" or char == "_":
                string += char
            else:
                break
    if string == name:
        print(name)
