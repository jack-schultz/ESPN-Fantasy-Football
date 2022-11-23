from espn_api.football import League
from pprint import PrettyPrinter
import os, time

printer = PrettyPrinter()

passwd = os.environ['password']

password = input("Enter password: ")
if password == passwd:
	swid_secret = os.environ['swid']
	espn_s2_secret = os.environ['espn_s2']
	league = League(league_id=174302610, year=2022, espn_s2=espn_s2_secret, swid=swid_secret)
else:
	swid = input("Enter swid: ")
	espn_s2 = input("Enter espn_s2: ")
	league_id = input("Enter league id: ")
	year = input("Enter year: ")
	league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)

os.system("clear")

def main(league):
	for i in range(len(league.teams)):
		print(f"{i+1}. {league.teams[i]}")
	print()
	your_team_list = []
	your_team = int(input("What team are you? > "))
	your_team_list.append(league.teams[your_team-1])
	os.system("clear")
	team = your_team_list[0]
	division_len = len(league.teams)
	while True:
		print(team)
		print(team.team_abbrev)
		print()
		print(f"{team.wins} - {team.losses} - {team.ties}")
		print(f"{team.standing} of {round(division_len)} - STANDINGS - {team.division_name}")
		denomenator = team.wins + team.losses
		numerator = team.wins
		percent = round(numerator/denomenator*100)
		print(f"WP: {percent}%")
		print(team.owner)
		print()
		print('''
1. View Roster
2. View Player Info
3. View Team Info
4. View Power Rankings
5. View Free Agents
6. View Recent Activity
7. View Box Score
8. View Standings
9. Random Things
10. Exit''')
		print()
		choice = int(input("What would you like to do? > "))
		if choice == 1:
			os.system("clear")
			print()
			for i in range(len(team.roster)):
				print(team.roster[i])
			print()
			input("Press enter to continue...")
		elif choice == 2:
			os.system("clear")
			print()
			for i in range(len(team.roster)):
				print(f"{i+1}. {team.roster[i]}")
			print()
			playerview = int(input("What player would you like to view? > "))
			player = team.roster[playerview-1]
			os.system("clear")
			print(player.name)
			print(f"TM: {player.proTeam}")
			print(f"POS: {player.position}")
			print(f'PRK: {player.posRank}')
			print(f'EPOS: {player.eligibleSlots}')
			print(f'AQST: {player.acquisitionType}')
			print(f'INGS: {player.injuryStatus}')
			print(f'INGD: {player.injured}')
			print(f"TOT: {player.total_points}")
			print(f"PTOT: {player.projected_total_points}")
			print(f"%ROST: {player.percent_owned}%")
			print(f"%ST: {player.percent_started}%")
			print("STATS: ")
			printer.pprint(player.stats)
			print()
			input("Press enter to continue...")
		elif choice == '':
			print("*INVALID*")
		elif choice == 4:
			os.system("clear")
			week = int(input("What week do you do you want to see the power rankings for? > "))
			for i in range(len(league.power_rankings(week=week))):
				print(f"{i+1}. {league.power_rankings(week=week)[i]}")
			time.sleep(2)
			print()
			input("Press enter to continue...")
		elif choice == 5:
			os.system('clear')
			pos = input('''What position do you want to see the free agents for?
QB
RB
WR
TE
FLEX
D/ST
K
All
> ''')
			print()
			
			if pos == 'ALL':
				free = league.free_agents()
				for i in range(len(free)):
					print(f"{free[i]}")
			else:
				free = league.free_agents(position=pos)
				for i in range(len(free)):
					print(f"{free[i]}")
				input("Press enter to continue...")

		elif choice == 6:
			os.system("clear")
			activity = league.recent_activity()
			activity_len = len(activity)
			for i in range(activity_len):
				print(f"{i+1}. {activity[i]}")
				print()
			input("Press enter to continue...")

		elif choice == 7:
			os.system("clear")
			box_scores = league.box_scores(10)
			for i in range(len(box_scores)):
				print(f"{i+1} -")
				print(box_scores[i].away_team)
				print(box_scores[i].home_team)
				print()

			box_score_choice = input("What matchup would you like to see the box score for? > ")
			box_score_matchup_away = box_scores[int(box_score_choice)-1].away_team
			box_score_matchup_home = box_scores[int(box_score_choice)-1].home_team
			box_score_away_score = box_scores[int(box_score_choice)-1].away_score
			box_score_home_score = box_scores[int(box_score_choice)-1].home_score
			away_lineup = list(box_scores[int(box_score_choice)-1].away_lineup)
			home_lineup = list(box_scores[int(box_score_choice)-1].home_lineup)
			os.system("clear")						  	
			away_home = input("Do you want to see the home team or away team boxscore? [a/h] > ")
			if away_home == 'a':
				os.system("clear")
				print(box_score_matchup_away)
				print(box_score_away_score)
				print()
				print(away_lineup)
				time.sleep(1)
				print()
				input("Press enter to continue...")
			elif away_home == 'h':
				os.system("clear")
				print(box_score_matchup_home)
				print(box_score_home_score)
				print()
				print(home_lineup)
				time.sleep(1)
				print()
				input("Press enter to continue...")

		elif choice == 8:
			os.system("clear")
			print()
			for i in range(len(league.standings())):
				print(f"{i+1}. {league.standings()[i]}")
			print()
			input("Press enter to continue...")
		
		elif choice == 10:
			os.system("clear")
			os.system("clear")
			menu_exit = input("Would you like to exit or view the team selection menu? [e/t] > ")
			if menu_exit == 'e':
				os.system("clear")
				exit()
			elif menu_exit == 't':
				os.system("clear")
				break
				
		elif choice == 3:
			os.system("clear")
			print(team)
			print(team.team_abbrev)
			print()
			print("STATS")
			print()
			print(f"{team.wins} - {team.losses} - {team.ties}")
			print(f"{team.standing} of {round(division_len)} - STANDINGS - {team.division_name}")
			print(f"%PLAYOFF: {team.playoff_pct}")
			winning_percentage = round(team.wins/team.losses * 100)
			print(f"WP: {winning_percentage}%")
			print(team.owner)
			print()
			print("POINTS")
			print()
			print(f"TTOT: {team.points_for}")
			print(f"FTOT: {team.points_against}")
			print()
			print("TRANSACTIONS")
			print()
			print(f"#AQUS: {team.acquisitions}")
			print(f"#DROPS: {team.drops}")
			print(f"#TRADES: {team.trades}")
			print()
			print("STREAKS")
			print()
			print(f"{team.streak_type} {team.streak_length}")
			print()
			print("SCHEDULE")
			print()
			print(team.schedule)
			print()
			input("Press enter to continue...")

		elif choice == 9:
			os.system("clear")
			print(f"WEEK TOP SCORER: {league.top_scorer()}")
			print(f"WEEK LEAST SCORER: {league.least_scorer()}")
			print(f"YEAR HIGHEST SCORER: {league.top_scored_week()}")
			print(f"YEAR LOWEST SCORER: {league.least_scored_week()}")
			print()
			input("Press enter to continue...")
			
		
			
		os.system("clear")


while True:
	main(league)




	
	
	
	


		
		



