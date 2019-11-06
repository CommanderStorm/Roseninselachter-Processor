import json

import mysql.connector


def importToJSON(p):
    mydb = mysql.connector.connect(user='root', password=p,
                                   host='127.0.0.1')
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT boots_id, renn_id, bootsname, steuerling_id, Athlet1ID, Athlet2ID, Athlet3ID, Athlet4ID, Athlet5ID, Athlet6ID, Athlet7ID, Athlet8ID FROM boote.boote")

    myresult = mycursor.fetchall()

    data = {}
    data['boote'] = []
    for x in myresult:
        boots_id, renn_id, bootsname, steuerling_id, Athlet1ID, Athlet2ID, Athlet3ID, Athlet4ID, Athlet5ID, Athlet6ID, Athlet7ID, Athlet8ID = x
        data['boote'].append({
            'boots_id': boots_id,
            'renn_id': renn_id,
            'bootsname': bootsname,
            'Athleten': [steuerling_id, Athlet1ID, Athlet2ID, Athlet3ID, Athlet4ID, Athlet5ID, Athlet6ID, Athlet7ID,
                         Athlet8ID]
        })
    mydb.close()
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
