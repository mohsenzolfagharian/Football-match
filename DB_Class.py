import sqlite3


# define database and it functions to modify data
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('table_league')

    def create_table(self, season):
        cur = self.conn.cursor()
        cur.execute(f"CREATE TABLE league{season} (teams TEXT, ga INT, gf INT, win INT, draw INT, lose INT);")
        # cur.close()

    def insert_teams(self, table_name, team_name):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO {table_name} (teams) VALUES('{team_name}');")
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
    

