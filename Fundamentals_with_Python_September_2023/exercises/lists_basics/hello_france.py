items_and_prices = input().replace("->", " ").replace("|", " ").split()
budget = float(input())
list_with_new_prices = []
profit = 0

for item in range(len(items_and_prices) // 2):
    current_item = items_and_prices[0]
    item_cost = float(items_and_prices[1])
    markup_price = 0

    if current_item == "Clothes":
        if budget >= item_cost <= 50:
            budget -= item_cost
            markup_price = item_cost + item_cost * 0.40
            list_with_new_prices.append(markup_price)

    elif current_item == "Shoes":
        if budget >= item_cost <= 35:
            budget -= item_cost
            markup_price = item_cost + item_cost * 0.40
            list_with_new_prices.append(markup_price)

    elif current_item == "Accessories":
        if budget >= item_cost <= 20.5:
            budget -= item_cost
            markup_price = item_cost + item_cost * 0.40
            list_with_new_prices.append(markup_price)

    if markup_price > 0:
        profit += markup_price - item_cost

    del items_and_prices[0:2]

for i in list_with_new_prices:
    budget += i
    print(f"{i:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")