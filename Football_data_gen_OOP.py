import random

result = None


class Teams:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.points = self.gf = self.ga = self.wins = self.draws = self.losses = 0

    def name_team(self):
        return self.name

    def power_team(self):
        return self.power
    
    def add_goal(self):
        self.gf += 1


class league:
    def goals_number(self):
        global result
        possible_goal_number_range = random.randint(0, 101)

        if possible_goal_number_range < 76:
            result = random.randint(1, 3)

        elif possible_goal_number_range < 86:
            result = random.randint(3, 6)

        elif possible_goal_number_range < 95:
            result = random.randint(6, 10)

        elif possible_goal_number_range < 99:
            result = random.randint(10, 20)

        elif possible_goal_number_range < 100:
            result = random.randint(20,31)


        # return result, possible_goal_number_range
        return result

    def match_result(self, goals, strng1, strng2, name1, name2):
        result = {name1:0, name2:0}
        teams_plate = []

        for x in range(strng1):
            teams_plate.append(name1)
        for x in range(strng2):
            teams_plate.append(name2)

        random.shuffle(teams_plate)

        for x in range(goals):
            goal = random.choice(teams_plate)
            if goal in teams_plate:
                result[goal] += 1
        return result

    def face2face_mathces(self, list_teams):
        for x in range(len(list_teams)):
            c = 1
            # inja bayad facae 2 face ijad konim :)
            while c <= len(list_teams):
                try:
                    goals = self.goals_number()
                    reslut_match = self.match_result(goals, list_teams[x][1].power_team(),
                                                          list_teams[x + c][1].power_team(),
                                                          list_teams[x][1].name_team(),
                                                          list_teams[x + c][1].name_team())
                    print(reslut_match)
                    c += 1
                except IndexError:
                    break

# define teams

# mohsen = Teams('mohsen', 70)
# mohammad = Teams('mohammad', 50)
# ali = Teams('ali', 40)
#
# # run leage
# test_leage = league()
#
# # possible goals for each game
# goals = test_leage.goals_number()
#
# # every game result
# result = test_leage.match_result(goals=goals, strng1=mohsen.power, strng2=mohammad.power, name1=mohsen.name, name2=mohammad.name)
#
# print(result)
