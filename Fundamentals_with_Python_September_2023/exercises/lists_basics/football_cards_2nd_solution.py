red_cards = input().split()
team_a_players = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b_players = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
is_terminated = False
for current_card in red_cards:
    if current_card in team_a_players:
        team_a_players.remove(current_card)
    elif current_card in team_b_players:
        team_b_players.remove(current_card)
    if len(team_a_players) < 7 or len(team_b_players) < 7:
        is_terminated = True
        break
print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
if is_terminated:
    print("Game was terminated")