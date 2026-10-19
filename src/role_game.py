from .character import Protagonist
from .game_reader import GameReader
from .items import Item

GAME_COMMANDS = ['LOOK', 'SEARCH', 'GO', 'FIGHT', 'EXIT', 'PICKUP', 'EQUIP']


class Game:
    @staticmethod
    def print_commands() -> None:
        for s in sorted(GAME_COMMANDS):
            print(s)

    def goto(self, where: str) -> str:
        message = f'Cannot go to {where}'
        possible_goes = self.protagonist.location.possiblePaths_list
        for p in possible_goes:
            if p.name.upper() == where.upper():
                self.protagonist.location = p
                message = 'You go to ' + where
        return message

    def look_at(self, what: str) -> str:
        message = ''
        message += self.look_at_location(what)
        message += self.look_at_self(what)
        message += self.look_at_object(what)
        message += self.look_at_enemy(what)

        if not message:
            message = f'Cannot look at {what}'
        return message

    def look_at_enemy(self, what: str) -> str:
        message = ''
        possible_enemies = self.protagonist.location.enemies_list
        for e in possible_enemies:
            if e.name.upper() == what.upper():
                message = e.description if e.is_alive else 'You see a dead {e.name}'
        return message

    def look_at_object(self, what: str) -> str:
        message = ''
        possible_objects = self.protagonist.location.objects_list
        for o in possible_objects:
            if o.name.upper() == what.upper():
                message = o.description
        for o in self.protagonist.rucksack:
            if o.name.upper() == what.upper():
                message = o.description
        if self.protagonist.weaponInHand is not None and self.protagonist.weaponInHand.name.upper() == what.upper():
            message = f'{self.protagonist.weaponInHand.description}. You have it equipped'
        if self.protagonist.shieldInHand is not None and self.protagonist.shieldInHand.name.upper() == what.upper():
            message = f'{self.protagonist.shieldInHand.description}. You have it equipped'
        return message

    def look_at_self(self, what: str) -> str:
        message = ''
        if what.upper() == self.protagonist.location.name.upper():
            message = self.protagonist.location.description
        return message

    def look_at_location(self, what: str) -> str:
        message = ''
        possible_goes = self.protagonist.location.possiblePaths_list
        for p in possible_goes:
            if p.name.upper() == what.upper():
                message = f'You can see the {what} from here'
        return message

    def fight(self, who: str) -> str:
        message = f'There is no {who} to fight'
        enemies = self.protagonist.location.enemies_list
        for e in enemies:
            if e.name.upper() == who.upper():
                if e.is_alive:
                    e.kill()
                    message = f'You just killed the {who}'
                else:
                    message = f'{who} is already dead'
                break
        return message

    def search(self, what: str|None=None) -> str:
        message = ''
        if what is None or what.upper() == self.protagonist.location.name.upper():
            message = self.search_items_in_location(message)
        elif what.upper() == 'BACKPACK':
            message = self.search_items_in_backpack()
        else:
            message = self.search_items_on_enemy(what)
            if message == '':
                message = f'Cannot search {what}'
        return message

    def search_items_on_enemy(self, what: str) -> str:
        message = ''
        for e in self.protagonist.location.enemies_list:
            if e.name.upper() == what.upper():
                if not e.is_alive:
                    objects_list = e.object_list
                    if len(objects_list) == 0:
                        message = f'Found nothing in {what}'
                    else:
                        for o in objects_list:
                            message += f'You found a {o.name}\n'
                else:
                    message = f'You cannot search {what} while it is alive!'
        return message

    def search_items_in_backpack(self) -> str:
        objects_list = self.protagonist.rucksack
        message = 'You look in your backpack:'
        if len(objects_list) > 0:
            for o in objects_list:
                message += f'\n\tYou have a {o.name}'
        return message

    def search_items_in_location(self, message: str) -> str:
        objects_list = self.protagonist.location.objects_list
        if len(objects_list) == 0:
            message = 'Found nothing'
        else:
            for o in objects_list:
                message += f'You found a {o.name}\n'
        return message

    def pickup(self, what: str) -> str:
        message = ''
        message = self.pickup_from_floor(message, what)
        message = self.pickup_from_enemy(message, what)
        if message == '':
            message = f'Cannot pickup {what}'

        return message

    def pickup_from_enemy(self, message: str, what: str) -> str:
        if message == '':
            enemies_list = self.protagonist.location.enemies_list
            for e in enemies_list:
                if not e.is_alive:
                    objects_list = e.object_list
                    for o in objects_list:
                        if o.name.upper() == what.upper():
                            self.protagonist.rucksack.append(o)
                            objects_list.remove(o)
                            message = f'You just picked up a {what}'
                            break
        return message

    def pickup_from_floor(self, message: str, what: str) -> str:
        objects_list = self.protagonist.location.objects_list
        for o in objects_list:
            if o.name.upper() == what.upper():
                self.protagonist.rucksack.append(o)
                objects_list.remove(o)
                message = f'You just picked up a {what}'
                break
        return message

    def equip_item(self, what: str) -> str:
        message = f'You have no {what} to equip'
        item_list = self.protagonist.rucksack
        message = self.check_if_item_is_equiped(message, what)
        for o in item_list:
            if o.name.upper() == what.upper():
                if o.__name__() == 'Weapon':
                    message = self.equip_weapon(item_list, o, what)
                    break
                if o.__name__() == 'Shield':
                    message = self.equip_shield(item_list, o, what)
                    break
                message = f"You can't equip {what}"
                break
        return message

    def equip_shield(self, item_list: list[Item], o: Item, what: str) -> str:
        message = 'You equipped your ' + what
        if self.protagonist.shieldInHand is not None:
            item_list.append(self.protagonist.shieldInHand)
        self.protagonist.shieldInHand = o
        item_list.remove(o)
        return message

    def equip_weapon(self, item_list: list[Item], o: Item, what: str) -> str:
        message = 'You equipped your ' + what
        if self.protagonist.weaponInHand is not None:
            item_list.append(self.protagonist.weaponInHand)
        self.protagonist.weaponInHand = o
        item_list.remove(o)
        return message

    def check_if_item_is_equiped(self, message: str, what: str) -> str:
        if self.protagonist.shieldInHand is not None and self.protagonist.shieldInHand.name.upper() == what.upper():
            message = f'{what} is already equipped'
        if self.protagonist.weaponInHand is not None and self.protagonist.weaponInHand.name.upper() == what.upper():
            message = f'{what} is already equipped'
        return message

    # Play!
    def play_game(self) -> None:
        print('What do you wish to do?')
        self.print_commands()

        split_command = ['BEGIN']
        while split_command[0] != 'EXIT':
            command = input()
            split_command = command.split()
            split_command[0] = split_command[0].upper()

            if split_command[0] == 'LOOK':
                if len(split_command) == 1:
                    print(self.protagonist.location.get_full_description())
                else:
                    print(self.look_at(split_command[1]))
            elif split_command[0] == 'GO':
                if len(split_command) == 1:
                    print('Go where?')
                else:
                    where = split_command[1]
                    print(self.goto(where))
            elif split_command[0] == 'SEARCH':
                if len(split_command) == 1:
                    print(self.search())
                else:
                    print(self.search(split_command[1]))
            elif split_command[0] == 'FIGHT':
                if len(split_command) == 1:
                    print('Fight against what?')
                else:
                    print(self.fight(split_command[1]))
            elif split_command[0] == 'PICKUP':
                if len(split_command) == 1:
                    print('Pickup what?')
                else:
                    print(self.pickup(split_command[1]))
            elif split_command[0] == 'EQUIP':
                if len(split_command) == 1:
                    print('Equip what?')
                else:
                    print(self.equip_item(split_command[1]))
            elif split_command[0] == 'EXIT':
                print('bye')
            else:
                self.print_commands()

    # Loads a game
    def load(self, path: str) -> None:
        gr = GameReader()
        gr.parse_game(path)

        # 1 - Properly connect places (now we have only ids)
        # We need the places to be in order
        self.places_array = sorted(gr.place_list, key=lambda place: place.id)

        self.begin_place = self.places_array[0]
        for p in self.places_array:
            connection_ids = p.connections_list
            for j in connection_ids:
                p.add_path(self.places_array[j])

        # 2 - Place enemies to places
        self.enemies_array = gr.enemy_list
        for enemy in self.enemies_array:
            self.places_array[enemy.location].add_enemy(enemy)

        # 3 - Temporally make protagonist. In the future it also should be readen
        self.protagonist = Protagonist('Cris', 'Cris is a demo warrior')
        self.protagonist.location = self.begin_place

    # Returns true for loading a game, or false for exiting
    def load_or_exit(self) -> bool:
        print('load games/DemoGame.xml')  # for testing purposes

        split_command = ['0']
        while split_command[0] != 'EXIT':
            user_command = input('Type "load $GAME_PATH" for loading a new game.\n'
                                 'Type "exit" to exit program:\n')
            split_command = user_command.split()
            split_command[0] = split_command[0].upper()
            if split_command[0] == 'LOAD':
                if len(split_command) == 2:
                    try:
                        self.load(split_command[1])
                        return True
                    except OSError:
                        print('File ' + split_command[1] + " doesn't seem to exist")
                else:
                    print('Error occurred: syntax must be "load $GAME_DIR"')
        return False

    def __init__(self) -> None:
        self.places_array = None
        self.begin_place = None
        self.enemies_array = None
        self.protagonist = None


if __name__ == '__main__':
    game = Game()
    if game.load_or_exit():
        print('loading game')
        game.play_game()
    else:
        print('Exit game')
