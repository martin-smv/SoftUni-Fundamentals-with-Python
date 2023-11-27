def add_func(piece, composer, key, dictionary):
    if piece not in dictionary:
        dictionary[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")

    return dictionary


def remove_func(piece, dictionary):
    if piece in dictionary:
        dictionary.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return dictionary


def change_key_func(piece, key, dictionary):
    if piece in dictionary:
        dictionary[piece][1] = key
        print(f"Changed the key of {piece} to {key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return dictionary


number_of_pieces = int(input())

pieces_dict = {}
for i in range(number_of_pieces):
    some_text = input().split("|")
    piece = some_text[0]
    composer = some_text[1]
    key = some_text[2]
    pieces_dict[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split("|")

    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        pieces_dict = add_func(piece, composer, key, pieces_dict)

    elif command[0] == "Remove":
        piece = command[1]
        pieces_dict = remove_func(piece, pieces_dict)

    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        pieces_dict = change_key_func(piece, new_key, pieces_dict)


for piece in pieces_dict:
    composer = pieces_dict[piece][0]
    key = pieces_dict[piece][1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")