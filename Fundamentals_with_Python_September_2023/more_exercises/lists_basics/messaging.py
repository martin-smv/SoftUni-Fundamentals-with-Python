numbers = input().split()
some_string = input()
message = ""
for result in numbers:
    result.split()
    index = sum(map(int, result))
    if index > len(some_string) - 1:
        index = index - len(some_string)
    message += some_string[index]
    some_string = some_string[:index] + some_string[index + 1:]
print(message)