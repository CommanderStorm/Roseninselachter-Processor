import mysql

from Generate_Edges import generate_edges
from Import_to_JSON import importToJSON
from Output_to_Database import output
from Processing import processing

# SET @@global.time_zone = '+01:00';
findsolution = True
SQLPassword = ""
JSONDaten_Filename = 'data.txt'
while SQLPassword == "":
    SQLPassword: str = input("Please input the MYSQL Password for user [root]:\n\t>")


def stateHasChanged() -> bool:
    """
    :rtype: bool
    """
    mydb = mysql.connector.connect(user='root', password=SQLPassword,
                                   host='127.0.0.1')
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT StateHasChangedSinceLastImport FROM boote.processing")

    myresult = mycursor.fetchall()
    return myresult != 0


def currentlyAbleToProcess() -> bool:
    """
    :rtype: bool
    """
    mydb = mysql.connector.connect(user='root', password=SQLPassword,
                                   host='127.0.0.1')
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT Processing FROM boote.processing")

    myresult = mycursor.fetchall()
    return myresult == 1


test = True
while test:
    if findsolution:
        # if stateHasChanged():
        importToJSON(SQLPassword, JSONDaten_Filename)
        generate_edges(JSONDaten_Filename)
        # if not stateHasChanged():
        processing(JSONDaten_Filename)
        # if not stateHasChanged():
        output(SQLPassword, JSONDaten_Filename)
    findsolution = currentlyAbleToProcess()
    test = False
