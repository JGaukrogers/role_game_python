class Obj:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon (Obj):

    def __init__(self, name, description, attack):
        Obj.__init__(self, name, description)
        self.attack = attack


class Shield(Obj):

    def __init__(self, name, description, defense):
        Obj.__init__(name, description)
        self.defense = defense
