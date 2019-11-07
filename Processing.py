import json


def processing():
    with open('data.txt') as json_file:
        data = json.load(json_file)
    print(data['vertecies'])
