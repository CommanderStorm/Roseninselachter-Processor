import json


def generate_edges(JSONDaten_Filename):
    # opening current state-of-the-art
    with open(JSONDaten_Filename) as json_file:
        data = json.load(json_file)
    # intit
    vert: dict = data['vertecies']
    verteciekeys = set(vert.keys())
    print(verteciekeys)
    edges = dict()

    while len(verteciekeys) > 1:
        verteciekey1 = verteciekeys.pop()
        v1 = vert[verteciekey1]
        for verteciekey2 in verteciekeys:
            v2 = vert[verteciekey2]
            edgeweight = 0
            numberofpersonintersects = len(set(v1['athleten']).intersection(set(v2['athleten'])))
            edgeweight += numberofpersonintersects * 10000
            numberofboatintersects = len(set(v1['bootsname']).intersection(set(v2['bootsname'])))
            edgeweight += numberofboatintersects * 5000
            if edgeweight > 0:
                edges[str(verteciekey1) + "-" + str(verteciekey2)] = edgeweight
                print("edge: " + str(verteciekey1) + "-" + str(verteciekey2) + ": " + str(edgeweight))

    data['edges'] = edges

    # saving progress
    with open(JSONDaten_Filename, 'w') as outfile:
        json.dump(data, outfile)
