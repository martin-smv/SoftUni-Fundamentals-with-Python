user_points = {}
user_submissions = {}

while True:
    command = input()
    if "-" not in command:
        break

    command = command.split("-")

    if command[1] == "banned":
        username = command[0]
        del user_points[username]

    else:
        username = command[0]
        language = command[1]
        points = int(command[2])

        if username not in user_points.keys():
            user_points[username] = points
        if points > user_points[username]:
            user_points[username] = points

        if language not in user_submissions.keys():
            user_submissions[language] = 0
        user_submissions[language] += 1


print("Results:")
for username, points in user_points.items():
    print(f"{username} | {points}")

print("Submissions:")
for language, submissions in user_submissions.items():
    print(f"{language} - {submissions}")

