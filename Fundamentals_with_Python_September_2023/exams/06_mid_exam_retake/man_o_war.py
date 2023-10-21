pirate_ship = [int(s) for s in input().split(">")]
warship = [int(i) for i in input().split(">")]
maximum_health_capacity = int(input())


ship_sinks = False
while True:
    list_with_command = input().split()
    command = list_with_command[0]

    if command == "Retire":
        break

    if command == "Fire":
        index = int(list_with_command[1])
        if 0 > index or index >= len(warship):
            continue

        damage = int(list_with_command[2])
        warship[index] -= damage
        if warship[index] <= 0:
            ship_sinks = True
            print(f"You won! The enemy ship has sunken.")
            break

    elif command == "Defend":
        start_index = int(list_with_command[1])
        end_index = int(list_with_command[2])
        damage = int(list_with_command[3])
        if 0 > start_index \
                or start_index >= len(pirate_ship) \
                or 0 > end_index \
                or end_index >= len(pirate_ship):
            continue

        for current_index in range(start_index, end_index + 1):
            pirate_ship[current_index] -= damage
            if pirate_ship[current_index] <= 0:
                ship_sinks = True
                print("You lost! The pirate ship has sunken.")
                break

    elif command == "Repair":
        index = int(list_with_command[1])
        if 0 > index or index >= len(pirate_ship):
            continue

        health = int(list_with_command[2])
        pirate_ship[index] += health
        if pirate_ship[index] > maximum_health_capacity:
            pirate_ship[index] = maximum_health_capacity

    elif command == "Status":
        need_repair = [x for x in pirate_ship if x < maximum_health_capacity * 0.20]
        count_of_repairs_needed = len(need_repair)
        print(f"{count_of_repairs_needed} sections need repair.")

if not ship_sinks:
    print(f"Pirate ship status: {sum(pirate_ship)}\n"
          f"Warship status: {sum(warship)}")