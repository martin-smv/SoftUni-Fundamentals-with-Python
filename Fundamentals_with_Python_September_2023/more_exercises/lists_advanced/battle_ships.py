rows_of_the_field = int(input())
ships = [input().split() for s in range(rows_of_the_field)]
list_with_attacks = input().split()

destroyed_ships = 0
for current_attack in list_with_attacks:
    row = int(current_attack[0])
    index = int(current_attack[2])

    current_row = [int(s) for s in ships[row]]
    ship = int(current_row[index])
    if ship > 0:
        ship = ship - 1
        current_row[index] = current_row[index] - 1
        ships[row] = current_row
        if ship == 0:
            destroyed_ships += 1

print(destroyed_ships)
