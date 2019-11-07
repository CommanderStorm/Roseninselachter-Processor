import json

import mysql.connector


def importToJSON(SQLPassword, JSONDaten_Filename):
    # delete current data
    open(JSONDaten_Filename, 'w').close()

    # SQL-init
    mydb = mysql.connector.connect(user='root',
                                   password=SQLPassword,
                                   host='127.0.0.1')
    mycursor = mydb.cursor()
    # getting data from SQL
    mycursor.execute(
        "SELECT BootsID, RennID, Bootsname, SteuerlingID, Athlet1ID, Athlet2ID, Athlet3ID, Athlet4ID, Athlet5ID, "
        "Athlet6ID, Athlet7ID, Athlet8ID FROM boote.boote")
    myresult = mycursor.fetchall()
    mycursor.execute("UPDATE boote.processing SET StateHasChangedSinceLastImport = 0")
    mydb.close()

    # generating boote
    data = {'boote': []}
    for x in myresult:
        boots_id, renn_id, bootsname, steuerling_id, athlet1ID, athlet2ID, athlet3ID, athlet4ID, athlet5ID, athlet6ID, athlet7ID, athlet8ID = x
        data['boote'].append({
            'boots_id': boots_id,
            'renn_id': renn_id,
            'bootsname': bootsname,
            'athleten': [steuerling_id, athlet1ID, athlet2ID, athlet3ID, athlet4ID, athlet5ID, athlet6ID, athlet7ID,
                         athlet8ID]
        })

    # generating vertecies
    vertecies = dict()
    for verteciestmp in data['boote']:
        if not verteciestmp['renn_id'] in vertecies.keys():
            vertecies[verteciestmp['renn_id']] = {'boots_id': [], 'bootsname': [], 'athleten': []}

        vertecies[verteciestmp['renn_id']]['boots_id'].append(verteciestmp['boots_id'])
        if not verteciestmp['bootsname'] == '':
            vertecies[verteciestmp['renn_id']]['bootsname'].append(verteciestmp['bootsname'])
        for athletennametmp in verteciestmp['athleten']:
            vertecies[verteciestmp['renn_id']]['athleten'].append(athletennametmp)
    data['vertecies'] = vertecies

    # saving progress
    with open(JSONDaten_Filename, 'w') as outfile:
        json.dump(data, outfile)
