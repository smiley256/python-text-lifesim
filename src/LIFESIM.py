import json
import os
import random
import subprocess
import sys



class Player:
    def __init__(self, location):
        self.location = location


class Location:
    def __init__(self, name="Unnamed Room", type="ROOM", features=[], exits=[]):
        self.name = name
        self.type = type
        self.features = features
        self.exits = exits

with open("../data/lifesim/roomTypes.json", "r") as file:
    Location.roomTypes = json.load(file)

    
class Npc:
    def __init__(self, name):
        self.name = name


def defineCommands():

    global debugOperations
    global operations
    global actions

    debugOperations = [
        ["/LOCATION", "/LOC", "/WHEREAMI", "/WHERE"], 
        ["/EXECUTABLE", "/EXECUTABLEPATH", "/EXE", "/EXEPATH", "/PATH"], 
        ["/ARGUMENTS", "/ARGS"], 
        ["/TELEPORT", "/TP", "/TELE", "/GOTO", "/GO"]
    ]

    operations = [ # TODO add !HELP
        ["!QUIT", "!EXIT", "!CLOSE", "!STOP", "!END", "!Q"], 
        ["!RESTART", "!RESET", "!RELOAD", "!R"]
    ]

    actions = [
        ["EXAMINE", "X", "LOOK", "LOOK AT"]
    ]

# TODO move this /data/lifesim/content.py, and later convert it to JSON
def content():
    global room
    room = Location("Sample Room", "FOREST")

    global room2
    room2 = Location("House", "ROOM")

    global player
    player = Player(room)



def main():

    #print("DEBUG: sys.executable =", sys.executable)
    #print("DEBUG: sys.argv =", sys.argv)


    content()
    defineCommands()

    

    print()
    print("You are located in " + player.location.name + ".")
    print()
    
    from commandInterpreter import runCommandInterpreter
    runCommandInterpreter()

if __name__ == "__main__":
    main()