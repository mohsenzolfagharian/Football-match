from Football_data_gen_OOP import League


def matches_result_save_to_file(list_teams):
    league = League()
    file = open('data.txt', 'a')
    for x in range(len(list_teams)):
        c = 1
        while c <= len(list_teams):
            try:
                goals = league.goals_number()
                result_match = league.match_result(goals, list_teams[x], list_teams[x + c])
                file.write(str(result_match) + '\n')
                c += 1
            except IndexError:
                break
    file.close()

