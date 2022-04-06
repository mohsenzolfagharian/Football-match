from Football_data_gen_OOP import League
from DB_Class import DB
import create_league
import save_matches

database = DB()
my_league = League()


teams = create_league.teams_to_list()


# every season teams will face each other 2 time
for x in range(0, 2):
    save_matches.matches_result_save_to_file(teams)
