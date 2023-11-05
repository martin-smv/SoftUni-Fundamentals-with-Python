elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    quantity = int(elements[i + 1])
    bakery[key] = quantity

print(bakery)