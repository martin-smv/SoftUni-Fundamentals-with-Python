def replace_rep_chars(string):
    new_string = ""
    for i in range(len(string)):
        if len(new_string) > 0:
            if string[i] == new_string[len(new_string) - 1]:
                continue
        new_string += string[i]

    return new_string


some_string = input()

print(replace_rep_chars(some_string))