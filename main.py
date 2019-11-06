from Import_to_JSON import importToJSON
from Processing import processing
from Output_to_Database import output

findsolution = True


def stateHasChanged() -> bool:
    """
    :rtype: bool
    """
    return True


def main():
    global findsolution
    while True:
        if findsolution:
            if stateHasChanged():
                importToJSON()
            if not stateHasChanged():
                processing()
            if not stateHasChanged():
                output()


main()
