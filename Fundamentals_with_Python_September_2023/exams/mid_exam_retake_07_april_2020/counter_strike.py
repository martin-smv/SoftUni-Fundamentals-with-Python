energy = int(input())

command = input()
won_games_counter = 0
while command != "End of battle":
    distance = int(command)

    if energy - distance < 0:
        print(f"Not enough energy! Game ends with {won_games_counter} won battles and {energy} energy")
        break

    energy -= distance
    won_games_counter += 1

    if won_games_counter % 3 == 0:
        energy += won_games_counter

    command = input()

if command == "End of battle":
    print(f"Won battles: {won_games_counter}. Energy left: {energy}" )