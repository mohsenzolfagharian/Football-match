import random
from tempfile import tempdir 


def goal_number():
    possible_goal_number_range = random.randint(0, 101)
    
    if possible_goal_number_range < 76:
        result = random.randint(0, 3)
    
    elif possible_goal_number_range < 86:
        result = random.randint(3, 6)
    
    elif possible_goal_number_range < 95:
        result = random.randint(6, 10)
    
    elif possible_goal_number_range < 99:
        result = random.randint(10, 20)
    
    elif possible_goal_number_range < 100:
        result = random.randint(20,31)
    

    return result, possible_goal_number_range

def goal_result(goals, strng1, strng2):
    result = {'teamA':0, 'teamB':0}
    team_result = []
    
    for x in range(strng1):
        team_result.append('teamA')
    for x in range(strng2):
        team_result.append('teamB')
    
    random.shuffle(team_result)
    
    for x in range(goals):
        goal = random.choice(team_result)
        print(goal)
        if goal in team_result:
            result[goal] += 1
    # return max(result.values()), result
    return result

print(goal_result(5, 3, 2))