team_records = {}
continueInMenu = True

while continueInMenu:
    team_stats = []
    team_name = input("Enter the name of the team: ")
    wins = int(input(f"Enter the number of wins of {team_name}: "))
    team_stats.append(wins)
    losses = int(input(f"Enter the number of losses of {team_name}: "))
    team_stats.append(losses)
    team_records[team_name] = team_stats

    user_choice = int(input("Do you want to add another team? (1: Yes, 2: No): "))
    if user_choice == 2:
        continueInMenu = False

print("\nTEAMS: ", end="")
for team in team_records:
    print(team, end=", ")

team_names = list(team_records.keys())

wins_list = []
for team in team_records:
    wins_list.append(team_records[team][0])

losses_list = []
for team in team_records:
    losses_list.append(team_records[team][1])

max_wins_index = wins_list.index(max(wins_list))
print("\nTeam with the highest wins: ", team_names[max_wins_index])

max_losses_index = losses_list.index(max(losses_list))
print("Team with the highest losses: ", team_names[max_losses_index])

selected_team_name = input("\nEnter the name of the team: ")
for team in team_records:
    if team == selected_team_name:
        wins = team_records[team][0]
        total_games = wins + team_records[team][1]
        win_percentage = (wins / total_games) * 100
        print("Win percentage of", selected_team_name, ": ", "%.2f" % win_percentage)
