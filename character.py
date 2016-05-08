class Character:

    def kill(self):
        self.is_alive = False

    def __init__(self, name, description, alive=True):
        self.name = name
        self.description = description
        # alive = false -> character is dead
        self.is_alive = alive


class Enemy(Character):

    def __init__(self, name, description, level, object_list):
        Character.__init__(self, name, description, True)
        self.level = level
        self.object_list = object_list


class Protagonist(Character):

    def increase_level(self):
        self.level += 1

    def add_to_rucksack(self, obj):
        self.rucksack.append(obj)

    def __init__(self, name, description):
        Character.__init__(self, name, description, True)
        self.level = 1
        self.location = None
        self.rucksack = []
        self.weaponInHand = None
        self.shieldInHand = None
