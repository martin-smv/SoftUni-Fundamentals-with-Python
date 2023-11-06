def user_exist():
    for value in force_book.values():
        if user in value:
            return True
    return False


def side_exist():
    if side not in force_book.keys():
        return False
    return True


def remove_user():
    for value in force_book.values():
        if user in value:
            value.remove(user)
            break


force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    elif "|" in command:
        side, user = command.split(" | ")
        if user_exist():
            continue

        if not side_exist():
            force_book[side] = []
        force_book[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")
        if user_exist():
            remove_user()

        if not side_exist():
            force_book[side] = []

        force_book[side].append(user)
        print(f"{user} joins the {side} side!")

for side, users in force_book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
