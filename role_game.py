#!/usr/bin/env python3.4

from game_reader import GameReader
# from place import Place
from protagonist import Protagonist
GAME_COMMANDS = ["LOOK", "SEARCH", "GO", "FIGHT", "EXIT", "PICKUP"]


class Game:

    @staticmethod
    def print_commands():
        for s in sorted(GAME_COMMANDS):
            print(s)

    def goto(self, where):
        message = "Cannot go to " + where
        possible_goes = self.protagonist.location.possiblePaths_list
        for p in possible_goes:
            if p.name.upper() == where.upper():
                self.protagonist.location = p
                message = "You go to " + where
        return message

    def look_at(self, what):
        message = "Cannot look at " + what
        # Look at location?
        possible_goes = self.protagonist.location.possiblePaths_list
        for p in possible_goes:
            if p.name.upper() == what.upper():
                message = "You can see the " + what + " from here"

        if what.upper() == self.protagonist.location.name.upper():
            message = self.protagonist.location.description

        # todo: Look at object?
        # Look at enemy?
        possible_enemies = self.protagonist.location.enemies_list
        for e in possible_enemies:
            if e.name.upper() == what.upper():
                if e.is_alive:
                    message = e.description
                else:
                    message = "You see a dead " + e.name
        return message

    def fight(self, who):
        message = "There is no " + who + " to kill"
        enemies = self.protagonist.location.enemies_list
        for e in enemies:
            if e.name.upper() == who.upper():
                e.kill()
                message = "You just killed the " + who
                break
        return message

    # Play!
    def play_game(self):
        # TODO: code
        print("What do you wish to do?")
        self.print_commands()

        split_command = ["BEGIN"]
        while split_command[0] != "EXIT":
            command = input()
            split_command = command.split()
            split_command[0] = split_command[0].upper()

            if split_command[0] == "LOOK":
                if len(split_command) == 1:
                    print(self.protagonist.location.get_full_description())
                else:
                    print(self.look_at(split_command[1]))
            elif split_command[0] == "GO":
                if len(split_command) == 1:
                    print("Go where?")
                else:
                    where = split_command[1]
                    print(self.goto(where))
            elif split_command[0] == "SEARCH":
                print("searching")
            elif split_command[0] == "FIGHT":
                if len(split_command) == 1:
                    print("Fight against what?")
                else:
                    print(self.fight(split_command[1]))
                    # todo: fight desired enemy if possible
            elif split_command[0] == "PICKUP":
                if len(split_command) == 1:
                    print("Pickup what?")
                else:
                    # todo: pickup desired stuff if possible
                    pass
            elif split_command[0] == "EXIT":
                print("bye")
            else:
                self.print_commands()

    # Loads a game
    def load(self, path):
        #    tree = ET.parse(path)
        #    root = tree.getroot()
        gr = GameReader()
        gr.parse_game(path)

        # 1 - places fertig einrichten (liste mit places geben, bisher haben wir nur id's)
        # We need the places to be in order
        self.places_array = sorted(gr.place_list, key=lambda place: place.id)

        self.begin_place = self.places_array[0]
        for p in self.places_array:
            connection_ids = p.connections_list
            for j in connection_ids:
                p.add_path(self.places_array[j])

        # 2 - feinde zu den places weitergeben
        self.enemies_array = gr.enemy_list
        for enemy in self.enemies_array:
            self.places_array[enemy.location].add_enemy(enemy)

        # 3 - temporaer protagonist erzeugen. In der zukunft soll es auch gelesen werden
        self.protagonist = Protagonist("Cris", "Cris is a demo warrior")
        self.protagonist.location = self.begin_place

    # Returns true for loading a game, or false for exiting
    def load_or_exit(self):
        print("load games/DemoGame.xml")  # for testing purposes

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
