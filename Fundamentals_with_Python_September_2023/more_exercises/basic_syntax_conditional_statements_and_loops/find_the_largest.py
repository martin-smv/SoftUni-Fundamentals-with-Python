number = int(input())
number_as_string = str(number)
for digit in range(len(number_as_string)):
    max_number = "".join(sorted(str(number), reverse=True))
print(max_number)