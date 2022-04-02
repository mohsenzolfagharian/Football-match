from Football_data_gen_OOP import League, Teams
from DB_Class import DB

database = DB()
my_league = League()

tuple_teams_list = ('tottenham', 40), ('manchester united', 70), ('liverpool', 20), ('arsenal', 60), ('chelsea', 50), \
                   ('mancity', 80), ('leeds united', 50), ('everton', 55), ('newcastle', 40), ('westham', 35), \
                   ('wolverhamton', 45), ('leicster city', 60), ('aston villa', 20), ('watford', 25), ('burly', 15),\
                   ('norwich', 10), ('southampton', 30), ('brentford', 40), ('crystal palace', 35), ('brighton', 10)

list_team = []



# add teams to database
# for x in tuple_teams_list:
#     database.insert_teams('league1', x[0])
#     print(x[0])


# append teams from tuple to dict
# for x in tuple_teams_list:
#     list_team.append(Teams(x[0], x[1]))

# # every season teams will face each other 2 time
# for x in range(0, 2):
#     my_league.matches_result_save_to_file(list_team)

