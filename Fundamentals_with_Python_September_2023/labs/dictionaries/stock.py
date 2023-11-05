elements = input().split()
storage = {}

for i in range(0, len(elements), 2):
    food = elements[i]
    quantity = elements[i + 1]
    storage[food] = quantity

products_to_search = input().split()

for product in products_to_search:
    if product in storage.keys():
        quantity = storage[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")