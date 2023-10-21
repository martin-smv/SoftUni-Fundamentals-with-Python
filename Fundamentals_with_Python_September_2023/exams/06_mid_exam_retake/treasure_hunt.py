def loot_func(loot, items):
    for i in range(len(items)):
        if items[i] not in loot:
            loot.insert(0, items[i])


def drop_func(loot, index):
    if 0 <= index < len(loot):
        item = loot.pop(index)
        loot.append(item)


def steal_func(loot, count):
    stolen_items = []
    for i in range(count):
        stolen_items.insert(0, loot.pop())
        if len(loot) == 0:
            print(", ".join(stolen_items))
            break
    else:
        print(", ".join(stolen_items))


loot = input().split("|")

while True:
    command = input().split()
    current_command = command[0]

    if current_command == "Yohoho!":
        break

    elif current_command == "Loot":
        items = command[1:]
        loot_func(loot, items)

    elif current_command == "Drop":
        index = int(command[1])
        drop_func(loot, index)

    elif current_command == "Steal":
        count = int(command[1])
        steal_func(loot, count)

if len(loot) > 0:
    length_of_every_item = [len(s) for s in loot]
    average_gain = sum(length_of_every_item) / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")