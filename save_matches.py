from Football_data_gen_OOP import League
from create_league import teams_to_list
import pickle


# create a file to save the result of each match on text file
def matches_result_save_to_file(list_teams):
    league = League()
    data = {}
    file = open('data.pkl', 'wb')
    for x in range(len(list_teams)):
        c = 1
        while c <= len(list_teams):
            try:
                goals = league.goals_number()
                result_match = league.match_result(goals, list_teams[x], list_teams[x + c])
                # pickle.dump(result_match, file)
                data.update(result_match)
                # file.write(result_match)
                c += 1
            except IndexError:
                break
    # file.close()
    pickle.dump(data, file)


matches_result_save_to_file(teams_to_list())
