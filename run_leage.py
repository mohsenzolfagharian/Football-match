from Football_data_gen_OOP import league, Teams

my_league = league()

tuple_teams_list = ('barcelona', 40), ('manchester united', 70), ('liverpool', 20), ('juve', 60), ('chelsea', 50), \
                   ('mancity', 80)

teams = {}
result = {}
# append teams from tuple to dict
for x in tuple_teams_list:
    teams[x[0]] = Teams(x[0], x[1])

# make a listed teams to do face 2 face matches
list_teams = list(teams.items())
for x in range(0, 2):
    my_league.face2face_mathces(list_teams)
