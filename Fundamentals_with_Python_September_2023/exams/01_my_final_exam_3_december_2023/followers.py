account_information = {}

while True:
    command = input()
    if command == "Log out":
        break

    command = command.split(": ")

    if command[0] == "New follower":
        username = command[1]
        if username not in account_information.keys():
            account_information[username] = {"Likes": 0, "Comments": 0}

    elif command[0] == "Like":
        username = command[1]
        count = int(command[2])
        if username not in account_information.keys():
            account_information[username] = {"Likes": 0, "Comments": 0}
        account_information[username]["Likes"] += count

    elif command[0] == "Comment":
        username = command[1]
        if username not in account_information.keys():
            account_information[username] = {"Likes": 0, "Comments": 0}
        account_information[username]["Comments"] += 1

    elif command[0] == "Blocked":
        username = command[1]
        if username not in account_information:
            print(f"{username} doesn't exist.")
        else:
            del account_information[username]

number_of_followers = len(account_information)
print(f"{number_of_followers} followers")
for user, value in account_information.items():
    likes = value["Likes"]
    comments = value["Comments"]
    total_sum = likes + comments
    print(f"{user}: {total_sum}")