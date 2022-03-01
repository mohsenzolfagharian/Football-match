from operator import le
from Football_data_gen_OOP import league, Teams

my_league = league()

tuple_teams_list = ('barcelona', 40), ('manchester united', 70), ('liverpool', 20), ('juve', 60), ('chelsea', 50)

teams = {}
result = {}
# append teams from tuple to dict
for x in tuple_teams_list:
    teams[x[0]] = Teams(x[0], x[1])


list_teams = list(teams.items())
print()
for x in range(len(list_teams)):
    if x == len(list_teams) - 1:
        break
    goals = my_league.goal_number()
    reslut_match = my_league.match_result(goals, list_teams[x][1].power_team(), list_teams[x+1][1].power_team(), list_teams[x][1].name_team(), list_teams[x+1][1].name_team())
    print(reslut_match)
# print(teams)
# create a league sim
# for team in teams:
#     print(team)
#     goals = my_league.goal_number()
    # result_match = my_league.match_result(goals, team.power_team(), pass ,team.name_team(), )

