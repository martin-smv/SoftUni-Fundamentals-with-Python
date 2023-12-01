target_cities_dict = {}

command = input()
while command != "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city not in target_cities_dict.keys():
        target_cities_dict[city] = {"Population": population, "Gold": gold}
    else:
        target_cities_dict[city]["Population"] += population
        target_cities_dict[city]["Gold"] += gold

    command = input()

command = input()
while command != "End":
    command = command.split("=>")

    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])

        target_cities_dict[town]["Population"] -= people
        target_cities_dict[town]["Gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if target_cities_dict[town]["Population"] == 0 or target_cities_dict[town]["Gold"] == 0:
            del target_cities_dict[town]
            print(f"{town} has been wiped off the map!")

    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            target_cities_dict[town]["Gold"] += gold
            total_gold = target_cities_dict[town]["Gold"]
            print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")

    command = input()

if target_cities_dict:
    print(f"Ahoy, Captain! There are {len(target_cities_dict)} wealthy settlements to go to:")
    for city, value in target_cities_dict.items():
        people = value["Population"]
        gold = value["Gold"]
        print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
