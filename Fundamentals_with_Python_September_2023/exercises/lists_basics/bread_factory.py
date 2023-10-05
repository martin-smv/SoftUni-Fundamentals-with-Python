events = input().split("|")
energy = 100
coins = 100
day_is_completed = True
for element in events:
    elements = element.split("-")
    current_element = elements[0]
    value = int(elements[1])

    if current_element == "rest":
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif current_element == "order":
        if energy >= 30:
            print(f"You earned {value} coins.")
            energy -= 30
            coins += value
        else:
            print("You had to rest!")
            energy += 50

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {current_element}.")
        else:
            print(f"Closed! Cannot afford {current_element}.")
            day_is_completed = False
            break

if day_is_completed:
    print(f"Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")