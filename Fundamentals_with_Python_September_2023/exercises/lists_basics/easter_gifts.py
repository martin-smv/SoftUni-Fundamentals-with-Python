gifts = input().split()
command = input().split()
while command != ["No", "Money"]:
    if command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = "None"
    elif command[0] == "Required":
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == "JustInCase":
        last_gift = len(gifts) - 1
        gifts[last_gift] = command[1]
    command = input().split()
while "None" in gifts:
    gifts.remove("None")
for i in gifts:
    print(i, end=" ")