from Football_data_gen_OOP import league, Teams

my_league = league()

tuple_teams_list = ('barcelona', 40), ('manchester united', 70), ('liverpool', 20), ('juve', 60), ('chelsea', 50)

teams = {}
result = {}
# append teams from tuple to list
for x in tuple_teams_list:
    teams[x[0]] = Teams(x[0], x[1])
print(teams['juve'].power_team())
