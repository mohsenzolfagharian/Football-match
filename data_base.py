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
        cur.execute(f"INSERT INTO league1 (teams) VALUES('{team_name}');")
        conn.commit()
        conn.close()

    def delete_table(self, table_name):
        cur = conn.cursor()
        cur.execute(f"DROP TABLE {table_name};")
        cur.close()

    def add_data(self, table_name, team, ga=None, gf=None, win=None, draw=None, lose=None):
        cur = conn.cursor()
        cur.execute(f"UPDATE {table_name} SET ga={ga}, gf={gf} WHERE teams='{team}';")
        conn.commit()
        conn.close()


a = DB()
# a.Create_table(1)
# a.delete_table('league1')
a.insert_teams('league1', 'arsenal')
