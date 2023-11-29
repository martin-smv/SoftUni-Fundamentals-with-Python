def rate(plant, rating, plants_info):
    if plant in plants_info.keys():
        if len(plants_info[plant]) > 1:
            plants_info[plant][1] += rating
            plants_info[plant][2] += 1
        else:
            plants_info[plant].append(rating)
            plants_info[plant].append(1)
    else:
        print("error")

    return plants_info


def update(plant, new_rarity, plants_info):
    if plant in plants_info.keys():
        plants_info[plant][0] = new_rarity
    else:
        print("error")

    return plants_info


def reset(plant, plants_info):
    if plant in plants_info.keys():
        if len(plants_info[plant]) > 1:
            plants_info[plant][1] = 0
            plants_info[plant][2] = 0
    else:
        print("error")

    return plants_info


plants_information = {}

number = int(input())
for i in range(number):
    plants = input().split("<->")
    plant = plants[0]
    rarity = int(plants[1])
    plants_information[plant] = [rarity]

command = input()
while command != "Exhibition":
    command = command.split(": ")

    if command[0] == "Rate":
        new_command = command[1].split(" - ")
        plant = new_command[0]
        rating = int(new_command[1])
        plants_information = rate(plant, rating, plants_information)

    elif command[0] == "Update":
        new_command = command[1].split(" - ")
        plant = new_command[0]
        new_rarity = int(new_command[1])
        plants_information = update(plant, new_rarity, plants_information)

    elif command[0] == "Reset":
        plant = command[1]
        plants_information = reset(plant, plants_information)

    command = input()

print("Plants for the exhibition:")
for current_plant, values in plants_information.items():
    rarity = values[0]
    rating = values[1]
    number_of_ratings = values[2]
    if number_of_ratings > 0:
        average_rating = rating / number_of_ratings
    else:
        average_rating = 0
    print(f"- {current_plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
