import random
import sqlite3


# define teams class
class Teams:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.ga, self.gf, self.win, self.draw, self.lose = 0, 0, 0, 0, 0

    def name_team(self):
        return self.name

    def power_team(self):
        return self.power


# define league and matches class
class League:

    def goals_number(self):
        possible_goal_number_range = random.randint(0, 101)
        result = 0
        if possible_goal_number_range < 76:
            result = random.randint(1, 3)

        elif possible_goal_number_range < 86:
            result = random.randint(3, 6)

        elif possible_goal_number_range < 95:
            result = random.randint(6, 10)

        elif possible_goal_number_range < 99:
            result = random.randint(10, 20)

        elif possible_goal_number_range < 100:
            result = random.randint(20, 31)


        # return result, possible_goal_number_range
        return result

    def match_result(self, goals, team1, team2):
        result = {team1.name_team(): 0, team2.name_team(): 0}
        teams_plate = []

        for x in range(team1.power_team()):
            teams_plate.append(team1.name_team())
        for x in range(team2.power_team()):
            teams_plate.append(team2.name_team())

        random.shuffle(teams_plate)

        for x in range(goals):
            goal = random.choice(teams_plate)
            if goal in teams_plate:
                result[goal] += 1
        return result


