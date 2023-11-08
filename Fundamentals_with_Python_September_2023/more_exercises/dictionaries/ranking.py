contests_and_passwords = {}

while True:
    command = input()
    if command == "end of contests":
        break

    contest, password = command.split(":")
    contests_and_passwords[contest] = password


users_information = {}

while True:
    second_command = input()
    if second_command == "end of submissions":
        break

    contest, password, username, points = second_command.split("=>")
    points = int(points)

    if contest in contests_and_passwords.keys() and password == contests_and_passwords[contest]:
        if username not in users_information.keys():
            users_information[username] = {contest: points}

        else:
            if contest in users_information[username]:
                if points > users_information[username][contest]:
                    users_information[username][contest] = points

            else:
                users_information[username].update({contest: points})

sorted_users = {k: v for k, v in sorted(users_information.items())}
for key, value in sorted_users.items():
    sort = {k: v for k, v in sorted(value.items(), key=lambda x: -x[1])}
    sorted_users[key] = sort

best_users_stats = {}
for name, value in sorted_users.items():
    for points in value.values():
        if name not in best_users_stats:
            best_users_stats[name] = 0
        best_users_stats[name] += points

best_user = ""
best_points = 0

for name, points in best_users_stats.items():
    if points > best_points:
        best_user = name
        best_points = points

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")
for name, value in sorted_users.items():
    print(name)
    for course, points in value.items():
        print(f"#  {course} -> {points}")
