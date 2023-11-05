stock_data = {}

while True:
    elements = input()

    if elements == "statistics":
        break

    product, quantity = elements.split(": ")

    if product in stock_data:
        stock_data[product] += int(quantity)
    else:
        stock_data[product] = int(quantity)

total_products = len(stock_data)
total_quantity = sum(stock_data.values())

print("Products in stock:")

for product, quantity in stock_data.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")