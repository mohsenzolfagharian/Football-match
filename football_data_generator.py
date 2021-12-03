import random 


def goal_number():
    possible_goal_number_range = random.randint(1, 101)
    
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
    result = {"a":0, 'b': 0}
    for index in range(0, goals + 1):
        result['a'] += random.randint(0, strng1)
        result['b'] += random.randint(0, strng2)
        
    return result


print(goal_result(5, 3, 2))