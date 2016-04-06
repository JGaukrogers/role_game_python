#!/usr/bin/python3.4

import xml.etree.ElementTree as ET

from game_reader import GameReader

# Loads a game
def load(path):
    tree = ET.parse(path)
    root = tree.getroot()
    gr = GameReader()
    gr.parse_game(path)
    # For testing purposes
    # for place in root.iter('place'):
    #   print(place.find('name').text)


# Returns true for loading a game, or false for exiting
def load_or_exit():
    print("load games/DemoGame.xml")
    user_command = input("Type \"load $GAME_PATH\" for loading a new game.\nType \"exit\" to exit program:\n")
    split_command = user_command.split()
    if split_command[0].lower() == "load":
        if len(split_command) == 2:
            load(split_command[1])
            return True
        else:
            print("Error occured: syntax must be \"load $GAME_DIR\"")
            return False
    else:
        return False


if __name__ == '__main__':
    if load_or_exit():
        print("loading game")
    else:
        print("Exit game")