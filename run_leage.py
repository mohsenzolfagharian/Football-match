from Football_data_gen_OOP import league, Teams

my_league = league()

tuple_teams_list = ('barcelona', 40), ('manchester united', 70), ('liverpool', 20), ('juve', 60), ('chelsea', 50)

teams = {}
result = {}
# append teams from tuple to dict
for x in tuple_teams_list:
    teams[x[0]] = Teams(x[0], x[1])


list_teams = list(teams.items())
for x in range(0, 2):
    my_league.face2face_mathces(list_teams)
# for x in range(len(list_teams)):
#     c = 1
#     # inja bayad facae 2 face ijad konim :)
#     while c <= len(list_teams):
#         try:
#             goals = my_league.goals_number()
#             reslut_match = my_league.match_result(goals, list_teams[x][1].power_team(), list_teams[x+c][1].power_team(),
#                                                   list_teams[x][1].name_team(), list_teams[x+c][1].name_team())
#             print(reslut_match)
#             c += 1
#         except IndexError:
#             break
