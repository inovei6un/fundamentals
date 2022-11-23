info = input().split(' ')
team_a_players = 11
team_b_players = 11

players_out = []

for card in info:
    if card not in players_out:
        players_out.append(card)
        if "A" in card:
            team_a_players -= 1
        else:
            team_b_players -= 1
    if team_a_players < 7 or team_b_players < 7:
        print(f"Team A - {team_a_players}; Team B - {team_b_players}")
        print(f"Game was terminated")
        quit()
print(f"Team A - {team_a_players}; Team B - {team_b_players}")
