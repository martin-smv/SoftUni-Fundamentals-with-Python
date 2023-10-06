numbers_strings = input().replace(",", "").split()
numbers_integers = []
for i in numbers_strings:
    numbers_integers.append(int(i))
for i in range(len(numbers_integers)):
    numbers_integers.append(numbers_integers.pop(numbers_integers.index(0)))
print(numbers_integers)