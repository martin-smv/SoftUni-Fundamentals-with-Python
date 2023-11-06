def register():
    username = command[1]
    plate_number = command[2]

    if username not in registered_users.keys():
        registered_users[username] = plate_number
        print(f"{username} registered {plate_number} successfully")
    else:
        print(f"ERROR: already registered with plate number {plate_number}")


def unregister():
    username = command[1]

    if username in registered_users.keys():
        del registered_users[username]
        print(f"{username} unregistered successfully")
    else:
        print(f"ERROR: user {username} not found")


number = int(input())

registered_users = {}
for i in range(number):
    command = input().split()

    if command[0] == "register":
        register()

    elif command[0] == "unregister":
        unregister()

for name, plate in registered_users.items():
    print(f"{name} => {plate}")