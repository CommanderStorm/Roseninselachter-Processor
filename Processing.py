import json


def processing():
    data = {}
    with open('data.txt') as json_file:
        data = json.load(json_file)
    print(data)
