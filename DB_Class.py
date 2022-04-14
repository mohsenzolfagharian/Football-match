import sqlite3
import json
from read_result_from_saved_file import read
from create_league import tuple_teams_list


# define database and it functions to modify data
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('table_league')

    def create_table(self, table_name):
        cur = self.conn.cursor()
        cur.execute(f"CREATE TABLE {table_name} (teams TEXT, ga INT, gf INT, win INT, draw INT, lose INT);")
        # cur.close()

    def insert_teams(self, table_name):
        cur = self.conn.cursor()
        for team in tuple_teams_list:
            cur.execute(f"INSERT INTO {table_name} (teams) VALUES('{team[0]}');")
            self.conn.commit()
        # cur.close()
        # self.conn.close()

    def delete_table(self, table_name):
        cur = self.conn.cursor()
        cur.execute(f"DROP TABLE {table_name};")
        # cur.close()

    def delete_team(self, table_name, team):
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE teams={team};")
        self.conn.commit()

    def update_info(self, table_name, team, col, value):
        cur = self.conn.cursor()
        cur.execute(f"UPDATE {table_name} SET {col}={value} WHERE teams='{team}';")
        self.conn.commit()

    def show_all(self, table_name):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {table_name};")
        data = cur.fetchall()
        return data

    def add_column(self, table_name, name, col_type):
        cur = self.conn.cursor()
        cur.execute(f'ALTER TABLE {table_name} ADD {name} {col_type};')

    def save(self):
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
            self.update_info('league1', team, 'gf', teams[team]['gf'])
            self.update_info('league1', team, 'ga', teams[team]['ga'])
            self.update_info('league1', team, 'win', teams[team]['win'])
            self.update_info('league1', team, 'lose', teams[team]['lose'])
            self.update_info('league1', team, 'draw', teams[team]['draw'])

    def points_calc(self, table_name):
        cur = self.conn.cursor()
        from create_league import tuple_teams_list
        for team in tuple_teams_list:
            team = team[0]
            cur.execute(f"SELECT win, draw FROM {table_name} where teams='{team}'")
            win_draw = cur.fetchall()
            points = (win_draw[0][0] * 3) + (win_draw[0][1])
            # cur.execute(f"UPDATE {table_name} SET points={points} WHERE teams='{team}';")
            self.update_info('league1', team, 'points', points)
            self.conn.commit()

    def order_by_points(self, table_name):
        cur = self.conn.cursor()
        cur.execute(f'SELECT * FROM {table_name} ORDER BY points DESC;')
        data = cur.fetchall()
        print(data)


d = DB()
d.points_calc('league1')

