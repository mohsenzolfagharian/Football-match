from Football_data_gen_OOP import League
import create_league
import save_matches
import save_to_db
my_league = League()

# call listed teams
teams = create_league.teams_to_list()


# every season teams will face each other 2 time
for x in range(0, 2):
    # save result of every match to a file
    save_matches.matches_result_save_to_file(teams)
    save_to_db.save()

