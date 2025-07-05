# NOT INTENDED FOR DIRECT USAGE

import json
import os
import random
import subprocess
import sys

main = sys.modules["__main__"]

def runCommandInterpreter():

    cmd = input("> ").strip().upper()

    if cmd in main.debugOperations[0]: # /LOCATION

        print()
        print("<DEBUG> Location name: " + main.player.location.name + ".")
        print("<DEBUG> Location type: " + main.player.location.type)
        print("<DEBUG> Features: " + ", ".join(main.player.location.features))
        print("<DEBUG> Exits: " + ", ".join(main.player.location.exits))
    
    elif cmd in main.debugOperations[1]: # /EXECUTABLE

        print()
        print("<DEBUG> Executable path: " + sys.executable)
        print("<DEBUG> Executable name: " + os.path.basename(sys.executable))
    
    elif cmd in main.debugOperations[2]: # /ARGUMENTS

        print()
        print("<DEBUG> Arguments: " + " ".join(sys.argv))
    
    elif cmd in main.debugOperations[3]: # /TELEPORT

        print()
        main.player.location = main.room2
        print("<DEBUG> Teleported to: " + main.player.location.name)

    elif cmd in main.operations[0]: # !QUIT

        sys.exit(0)
    
    elif cmd in main.operations[1]: # !RESTART

        print()
        print("Restarting...")

        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit(0)

    elif cmd in main.actions[0]: # EXAMINE
        
        print()
        print("You examine the the surrounding area. You see:")
        print(random.choice(main.Location.roomTypes[main.player.location.type]["DESCRIPTION"]))
    
    else:

        print()
        print("Invalid command! Please enter a valid command.")
        print("Inputted command: " + cmd)
    
    runCommandInterpreter()