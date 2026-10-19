class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __name__(self):
        return "Item"


class Weapon (Item):

    def __init__(self, name, description, attack):
        Item.__init__(self, name, description)
        self.attack = attack

    def __name__(self):
        return "Weapon"


class Shield(Item):

    def __init__(self, name, description, defense):
        Item.__init__(self, name, description)
        self.defense = defense

    def __name__(self):
            return "Shield"
