#!/usr/bin/python3.4

from game_reader import GameReader
# from place import Place
from protagonist import Protagonist
GAME_COMMANDS = ["LOOK", "SEARCH", "GO", "FIGHT","EXIT", "PICKUP"];


class Game:

    @staticmethod
    def __print_commands():
        for s in sorted(GAME_COMMANDS):
            print(s)

    # Play!
    def play_game(self):
        # TODO: code
        print("What do you wish to do?")
        self.__print_commands()

        split_command = ["BEGIN"]
        while split_command[0] != "EXIT":
            command = input()
            split_command = command.split()
            split_command[0] = split_command[0].upper()

            if split_command[0] == "LOOK":
                if len(split_command) == 1:
                    # todo: print current location
                    pass
                else:
                    # todo: print desired stuff
                    pass
            elif split_command[0] == "GO":
                print("going to some place")
            elif split_command[0] == "FIGHT":
                print("fighting")
            elif split_command[0] == "EXIT":
                print("bye")
            else:
                self.__print_commands()

    # Loads a game
    def load(self, path):
        #    tree = ET.parse(path)
        #    root = tree.getroot()
        gr = GameReader()
        gr.parse_game(path)

        # 1 - places fertig einrichten (liste mit places geben, bisher haben wir nur id's)
        # We need the places to be in order
        self.places_array = sorted(gr.get_places_list(), key=lambda place: place._id)

        self.begin_place = self.places_array[0]
        for p in self.places_array:
            connection_ids = p.get_connection_ids()
            for j in connection_ids:
                p.add_path(self.places_array[j])

        # 2 - feinde zu den places weitergeben
        self.enemies_array = gr.get_enemies_list()

        # 3 - temporaer protagonist erzeugen. In der zukunft soll es auch gelesen werden
        self.protagonist = Protagonist("Cris", "Cris is a demo warrior")

    # Returns true for loading a game, or false for exiting
    def load_or_exit(self):
        print("load games/DemoGame.xml") # for testing purposes

        split_command = ["0"]
        while split_command[0] != "EXIT":
            user_command = input("Type \"load $GAME_PATH\" for loading a new game.\nType \"exit\" to exit program:\n")
            split_command = user_command.split()
            split_command[0] = split_command[0].upper()
            if split_command[0] == "LOAD":
                if len(split_command) == 2:
                    self.load(split_command[1])
                    return True
                else:
                    print("Error occurred: syntax must be \"load $GAME_DIR\"")
        return False

    def __init__(self):
        self.places_array = None
        self.begin_place = None
        self.enemies_array = None
        self.protagonist = None


if __name__ == '__main__':
    game = Game()
    if game.load_or_exit():
        print("loading game")
        game.play_game()
    else:
        print("Exit game")
