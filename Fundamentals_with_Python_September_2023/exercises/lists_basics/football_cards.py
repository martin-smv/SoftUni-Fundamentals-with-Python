red_cards = input().split()
team_a_players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b_players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_terminated = False
for cards in red_cards:
    if "A" in cards:
        new_string = cards.replace("A-", "")
        if int(new_string) in team_a_players:
            team_a_players.remove(int(new_string))
    elif "B" in cards:
        new_string = cards.replace("B-", "")
        if int(new_string) in team_b_players:
            team_b_players.remove(int(new_string))
    if len(team_a_players) < 7 or len(team_b_players) < 7:
        is_terminated = True
        break
if is_terminated:
    print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
    print("Game was terminated")
else:
    print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")