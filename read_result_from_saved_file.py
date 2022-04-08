import ast
import json

# read data from saved file , and it needed to get better
import pickle


def read():
    data_as_json = {}
    f = open('data.txt', 'r')
    lines = f.readlines()
    # print(lines)
    for line in lines:
        if line == " ":
            pass
        cleaned_line = line.replace("\n", "")
        print(cleaned_line)
        data_as_json.update(map(json.loads, cleaned_line))

    # return data_as_json
    # return data_as_json


def test_read():
    file = open("data.pkl", "rb")
    loaded_data = pickle.load(file)
    return loaded_data

# read()

print(test_read())
print(len(test_read()))

