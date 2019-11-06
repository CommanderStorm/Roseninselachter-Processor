from Import_to_JSON import importToJSON
from Output_to_Database import output
from Processing import processing

findsolution = True


def stateHasChanged() -> bool:
    """
    :rtype: bool
    """
    return True


test = True
while test:
    if findsolution:
        if stateHasChanged():
            importToJSON(input("Please input the MYSQL Password for user [root]:\n\t>"))
        if not stateHasChanged():
            processing()
        if not stateHasChanged():
            output()
    test = False
