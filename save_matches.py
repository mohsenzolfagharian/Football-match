from Football_data_gen_OOP import League
from create_league import teams_to_list


# create a file to save the result of each match on text file
def matches_result_save_to_file(list_teams):
    league = League()
    file = open('data.txt', 'w')
    for x in list_teams:
        for y in list_teams:
            if x.name_team() == y.name_team():
                continue
            goals = league.goals_number()
            result_match = league.match_result(goals, x, y)
            st = str(result_match)
            file.write(f"{st}" + "\n")
    file.close()


# matches_result_save_to_file(teams_to_list())
