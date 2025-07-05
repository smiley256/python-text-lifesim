import json
import os
import random
import subprocess
import sys

class Player:
    def __init__(self, location):
        self.location = location


class Location:
    def __init__(self, name="Room", type="ROOM", features=[], surroundings=[]):
        self.name = name
        self.type = type
        self.features = features
        self.surroundings = surroundings

with open("../data/lifesim/roomTypes.json", "r") as file:
    Location.roomTypes = json.load(file)

    
class Npc:
    def __init__(self, name):
        self.name = name


debugOperations = [
    ["/LOCATION", "/LOC", "/WHEREAMI", "/WHERE"], 
    ["/EXECUTABLE", "/EXECUTABLEPATH", "/EXE", "/EXEPATH", "/PATH"], 
    ["/ARGUMENTS", "/ARGS"]
]

operations = [
    ["!QUIT", "!EXIT", "!CLOSE", "!STOP", "!END", "!Q"], 
    ["!RESTART", "!RESET", "!RELOAD", "!R"]
]

actions = [
    ["EXAMINE", "X", "LOOK", "LOOK AT"]
]

def content():
    global room
    room = Location("Sample Room", "FOREST", [], [])

    global player
    player = Player(room)


def runCommandInterpreter():

    cmd = input("> ").strip().upper()

    if cmd in debugOperations[0]: # /LOCATION

        print()
        print("<DEBUG> You are currently in " + player.location.name + ".")
        print("<DEBUG> Location type: " + player.location.type)
        print("<DEBUG> Features: " + ", ".join(player.location.features))
        print("<DEBUG> Surroundings: " + ", ".join(player.location.surroundings))
    
    elif cmd in debugOperations[1]: # /EXECUTABLE

        print()
        print("<DEBUG> Executable path: " + sys.executable)
        print("<DEBUG> Executable name: " + os.path.basename(sys.executable))
    
    elif cmd in debugOperations[2]: # /ARGUMENTS

        print()
        print("<DEBUG> Arguments: " + " ".join(sys.argv))

    elif cmd in operations[0]: # !QUIT

        sys.exit(0)
    
    elif cmd in operations[1]: # !RESTART

        print()
        print("Restarting...")

        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit(0)

    elif cmd in actions[0]:
        
        print()
        print("You examine the the surrounding area. You see:")
        print(random.choice(Location.roomTypes[player.location.type]["DESCRIPTION"]))
    
    runCommandInterpreter()


def main():

    #print("DEBUG: sys.executable =", sys.executable)
    #print("DEBUG: sys.argv =", sys.argv)

    content()

    print()
    print("You are located in " + player.location.name + ".")
    print()

    runCommandInterpreter()

if __name__ == "__main__":
    main()