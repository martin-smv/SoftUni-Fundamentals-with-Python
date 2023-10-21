neighborhood = [int(s) for s in input().split("@")]

command = input()
index = 0
while command != "Love!":
    current_command = command.split()
    jump_length = int(current_command[1])
    index += jump_length

    if index >= len(neighborhood):
        index = 0

    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
        command = input()
        continue
    neighborhood[index] -= 2
    if neighborhood[index] == 0:
        print(f"Place {index} has Valentine's day.")

    command = input()

failed_houses = 0
for house in neighborhood:
    if house > 0:
        failed_houses += 1

print(f"Cupid's last position was {index}.")
if failed_houses == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")
