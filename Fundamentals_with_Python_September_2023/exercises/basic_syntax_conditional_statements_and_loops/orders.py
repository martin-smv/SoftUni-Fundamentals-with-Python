number_of_orders = int(input())

total_price = 0
for information in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())
    price_for_the_coffee = (price_per_capsule * needed_capsules_per_day) * days

    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue
    elif 1 > days or days > 31:
        continue
    elif 1 > needed_capsules_per_day or needed_capsules_per_day > 2000:
        continue
    total_price += price_for_the_coffee
    print(f"The price for the coffee is: ${price_for_the_coffee:.2f}")
print(f"Total: ${total_price:.2f}")