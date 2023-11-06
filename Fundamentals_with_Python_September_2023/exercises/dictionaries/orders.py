products = {}

while True:
    current_product = input()
    if current_product == "buy":
        break

    name, price, quantity = current_product.split()

    if name not in products.keys():
        products[name] = [float(price), int(quantity)]
    else:
        products[name][0] = float(price)
        products[name][1] += int(quantity)

for product, values in products.items():
    price = values[0]
    quantity = values[1]
    total_cost = price * quantity
    print(f"{product} -> {total_cost:.2f}")
