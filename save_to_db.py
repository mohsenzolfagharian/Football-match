from DB_Class import DB
from read_result_from_saved_file import read
import json

db = DB()


def save():
    data = read()
    teams = {}
    for match in range(len(data)):
        as_js = json.loads(data[match])
        team1, team2 = as_js.keys()
        teams[team1] = {"gf": 0, "ga": 0, "win": 0, "lose": 0, "draw": 0}
        teams[team1] = {"gf": 0, "ga": 0, "win": 0, "lose": 0, "draw": 0}
    for goal in range(len(data)):
        as_js = json.loads(data[goal])
        gt1, gt2 = as_js.values()
        team1, team2 = as_js.keys()
        teams[team1]['ga'] += gt1
        teams[team1]['gf'] += gt2
        teams[team2]['ga'] += gt2
        teams[team2]['gf'] += gt1
        if gt1 > gt2:
            teams[team1]["win"] += 1
            teams[team2]["lose"] += 1
        elif gt2 > gt1:
            teams[team2]["win"] += 1
            teams[team1]["lose"] += 1
        else:
            teams[team1]["draw"] += 1
            teams[team2]["draw"] += 1
    for team in teams:
        db.update_info('league1', team, 'gf', teams[team]['gf'])
        db.update_info('league1', team, 'ga', teams[team]['ga'])
        db.update_info('league1', team, 'win', teams[team]['win'])
        db.update_info('league1', team, 'lose', teams[team]['lose'])
        db.update_info('league1', team, 'draw', teams[team]['draw'])


print(save())

