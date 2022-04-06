import ast
import json


def read():
    data_as_json = {}
    f = open('data.txt', 'r')
    lines = f.readlines()
    lines = str(lines)
    data_as_json = json.loads(lines)
    return data_as_json
    # return data_as_json


print(read())
