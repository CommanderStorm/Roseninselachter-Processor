import json


def processing(JSONDaten_Filename):
    with open(JSONDaten_Filename) as json_file:
        data = json.load(json_file)
    print(data['vertecies'])
    print(data['edges'])
