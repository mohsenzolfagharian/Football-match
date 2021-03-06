from Football_data_gen_OOP import Teams

# create database object to work with db
tuple_teams_list = ('tottenham', 40), ('manchester united', 100), ('liverpool', 20), ('arsenal', 60), \
                   ('chelsea', 50), ('mancity', 80), ('leeds united', 50), ('everton', 55), ('newcastle', 40), \
                   ('westham', 35), ('wolverhamton', 45), ('leicster city', 60), ('aston villa', 20), \
                   ('watford', 25), ('burly', 15), ('norwich', 10), ('southampton', 30), ('brentford', 40), \
                   ('crystal palace', 35), ('brighton', 10)


# create a list of teams with their power
def teams_to_list():
    list_team = []
    for team in tuple_teams_list:
        list_team.append(Teams(team[0], team[1]))

    return list_team

