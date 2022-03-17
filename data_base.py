import sqlite3

conn = sqlite3.connect('table_league')


class DB:
    def __init__(self):
        pass

    def Create_table(self, season):
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE league{season} (teams TEXT, ga INT, gf INT, win INT, draw INT, lose INT);")
        cur.close()

    # def Add_data(self):
        # cur = conn.cursor()
        # cur.execute()

a = DB()
a.Create_table(1)

