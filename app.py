import copy

from constants import PLAYERS, TEAMS

players = copy.copy(PLAYERS)
teams = copy.copy(TEAMS)
data = players, teams


def clean_data(players):
    cleaned = []
    for player in players:
        height = int(player['height'].split()[0])

        if player["experience"] == "YES":
            experience = True
        else:
            experience = False

        cleaned.append({
            "name": player['name'],
            "height": height,
            "experience": experience
        })
    return cleaned


def balance_teams(players, teams):
    num_players = len(players) // len(teams)
    balanced_teams = []
    for team in teams:
        players_on_team = players[:num_players]
        players = players[num_players:]
        balanced_teams.append({
            "team": team,
            "players": players_on_team
        })

    return num_players, balanced_teams


def main():
    # Logic here
    print("BASKETBALL TEAM STATS TOOL")

    print("\n-----MENU-----")
    print("\nHere are your choices:\n A) Display Team Stats \n B) Quit")
    menu = ['A', 'B', 'a', 'b']
    option = str(input("\nEnter your option:  "))

    while option not in menu:
        option = str(input("Enter your option:  "))

    if option == 'A' or option == 'a':
        print(f"\n A) {teams[0]}\n B) {teams[1]}\n C) {teams[2]}")
        team_choices = ['A', 'B', 'C', 'a', 'b', 'c']
        team_option = str(input("\nEnter your option:  "))

        while team_option not in team_choices:
            team_option = str(input("Enter your option:  "))

        if team_option == 'A' or team_option == 'a':
            team_index = 0
        elif team_option == 'B' or team_option == 'b':
            team_index = 1
        elif team_option == 'C' or team_option == 'c':
            team_index = 2
        else:
            exit()
    else:
        exit()

    selected_team = teams[team_index]
    number_of_players, balanced_teams = balance_teams(clean_data(players), teams)

    for team in balanced_teams:
        if team['team'] == selected_team:
            print(f"\nTeam: {selected_team} Stats")
            print("-----------------------")
            print(f"Total players: {number_of_players}")
            # assign the player names as strings separated by commas
            player_names = []
            for player in team['players']:
                player_names.append(player['name'])
            print(f"\nPlayers on Team:\n {', '.join(player_names)}")


if __name__ == "__main__":
    main()
