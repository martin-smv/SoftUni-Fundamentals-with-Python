total_cost_without_taxes = 0
total_taxes = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        break

    price = float(command)

    if price < 0:
        print("Invalid price!")
        continue

    elif price == 0:
        print("Invalid order!")
        continue

    total_cost_without_taxes += price
    total_taxes += price * 0.20

total_cost = total_cost_without_taxes + total_taxes

if total_cost == 0:
    print("Invalid order!")
    exit()

if command == "special":
    discount = total_cost * 0.10
    total_cost -= discount

print("Congratulations you've just bought a new computer!\n"
      f"Price without taxes: {total_cost_without_taxes:.2f}$\n"
      f"Taxes: {total_taxes:.2f}$\n"
      "-----------\n"
      f"Total price: {total_cost:.2f}$")