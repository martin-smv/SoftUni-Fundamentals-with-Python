submissions_info = {}

while True:
    command = input()
    if "->" not in command:
        break

    command = command.split(" -> ")
    username = command[0]
    contest = command[1]
    points = int(command[2])

    if contest not in submissions_info.keys():
        submissions_info[contest] = {username: points}
    else:
        if username in submissions_info[contest].keys():
            if points > submissions_info[contest][username]:
                submissions_info[contest][username] = points
        else:
            submissions_info[contest].update({username: points})

for key, value in submissions_info.items():
    sort = {k: v for k, v in sorted(value.items(), key=lambda x: (-x[1], x[0]))}
    submissions_info[key] = sort

summed_points = {}

for key, value in submissions_info.items():
    print(f"{key}: {len(value)} participants")
    number = 1
    for user, points in value.items():
        print(f"{number}. {user} <::> {points}")
        number += 1

        if user not in summed_points:
            summed_points[user] = 0
        summed_points[user] += points

sort_summed_points = {k: v for k, v in sorted(summed_points.items(), key=lambda x: (-x[1], x[0]))}

print("Individual standings:")
number = 1
for user, points in sort_summed_points.items():
    print(f"{number}. {user} -> {points}")
    number += 1
