def calculate_total_price(product_type, n):
    if product_type == 'coffee':
        return 1.50 * n
    elif product_type == 'coke':
        return 1.40 * n
    elif product_type == 'water':
        return 1.00 * n
    elif product_type == 'snacks':
        return 2.00 * n


product = input()
number_of_products = int(input())
result = calculate_total_price(product, number_of_products)
print(f"{result:.2f}")