class Obj:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon (Obj):

    def __init__(self, name, description, attack):
        Obj.__init__(self, name, description)
        self.attack = attack
