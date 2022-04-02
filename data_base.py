import sqlite3

conn = sqlite3.connect('table_league')


class DB:
    def __init__(self):
        pass

    def Create_table(self, season):
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE league{season} (teams TEXT, ga INT, gf INT, win INT, draw INT, lose INT);")
        cur.close()

    def insert_teams(self, table_name, team_name):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {table_name} (teams) VALUES('{team_name}');")
        conn.commit()
        cur.close()
        conn.close()

    def delete_table(self, table_name):
        cur = conn.cursor()
        cur.execute(f"DROP TABLE {table_name};")
        cur.close()

    def delete_team(self, table_name, team):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE teams={team};")
        conn.commit()
        conn.close()

    def update_info(self, table_name, team, col, value):
        cur = conn.cursor()
        cur.execute(f"UPDATE {table_name} SET {col}={value} WHERE teams='{team}';")
        conn.commit()
        conn.close()

    def show_all(self, table_name):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name};")
        data = cur.fetchall()
        conn.close()
        return data
    



a = DB()
# a.Create_table(1)
# a.update_info('league1', 'manchester', 'gf', 10)
# a.delete_table('league1')

# a.insert_teams('league1', 'real')

# a.delete_team("league1", "arsenal")

# a.add_gf('league1', 'manchester', 5)


# data = a.show_all('league1')
# for d in data:
#     print(d)


