rooms = input().split("|")

health = 100
bitcoins = 0
you_died = False
for current_room in rooms:
    current_room = current_room.split()
    command = current_room[0]
    number = int(current_room[1])

    if command == "potion":
        current_health = health
        health += number
        if health > 100:
            health = 100
        print(f"You healed for {health - current_health} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            index_of_the_best_room = [rooms.index(i) for i in rooms if i == " ".join(current_room)]
            best_room = index_of_the_best_room[0] + 1
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            you_died = True
            break

if not you_died:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")