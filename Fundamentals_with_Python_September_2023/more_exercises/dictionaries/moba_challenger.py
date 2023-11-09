players_info = {}

while True:
    command = input()
    if command == "Season end":
        break

    elif "->" in command:
        command = command.split(" -> ")
        player = command[0]
        position = command[1]
        skill = int(command[2])

        if player not in players_info.keys():
            players_info[player] = {position: skill}
        elif position not in players_info[player].keys():
            players_info[player].update({position: skill})
        else:
            if skill > players_info[player][position]:
                players_info[player] = {position: skill}

    elif "vs" in command:
        command = command.split(" vs ")
        first_player = command[0]
        second_player = command[1]

        if first_player in players_info.keys() and second_player in players_info.keys():
            for first_position in players_info[first_player].keys():
                for second_position in players_info[second_player].keys():

                    if first_position == second_position:
                        if players_info[first_player][first_position] > players_info[second_player][second_position]:
                            del players_info[second_player]
                            break
                        elif players_info[first_player][first_position] < players_info[second_player][second_position]:
                            del players_info[first_player]
                            break
                        else:
                            continue

                if first_position == second_position:
                    break

for key, value in players_info.items():
    for name, skill in value.items():
        players_info[key] = {k: v for k, v in sorted(value.items(), key=lambda x: (-x[1], x[0]))}

total_skill = {}
for name, value in players_info.items():
    total_skill[name] = 0
    for skill in value.values():
        total_skill[name] += skill

sorted_total_skill = {k: v for k, v in sorted(total_skill.items(), key=lambda x: (-x[1], x[0]))}

for player, skill in sorted_total_skill.items():
    print(f"{player}: {skill} skill")
    for position, current_skill in players_info[player].items():
        print(f"- {position} <::> {current_skill}")
