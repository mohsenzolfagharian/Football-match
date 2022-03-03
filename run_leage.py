from Football_data_gen_OOP import league, Teams

my_league = league()

tuple_teams_list = ('tottenham', 40), ('manchester united', 70), ('liverpool', 20), ('arsenal', 60), ('chelsea', 50), \
                   ('mancity', 80), ('leeds united', 50), ('everton', 55), ('newcastle', 40), ('westham', 35), \
                   ('wolverhamton', 45), ('leicster city', 60), ('aston villa', 20), ('watford', 25), ('burly', 15),\
                   ('norwich', 10), ('southampton', 30), ('brentford', 40), ('crystal palace', 35), ('brighton', 10)


teams = {}
result = {}
# append teams from tuple to dict
for x in tuple_teams_list:
    teams[x[0]] = Teams(x[0], x[1])

# make a listed teams to do face 2 face matches
list_teams = list(teams.items())
c = 0
# every season teams will face each other 2 time
for x in range(0, 20):
    my_league.face2face_mathces(list_teams)

