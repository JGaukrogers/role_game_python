class Obj:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __name__(self):
        return "Obj"


class Weapon (Obj):

    def __init__(self, name, description, attack):
        Obj.__init__(self, name, description)
        self.attack = attack

    def __name__(self):
        return "Weapon"


class Shield(Obj):

    def __init__(self, name, description, defense):
        Obj.__init__(self, name, description)
        self.defense = defense

    def __name__(self):
            return "Shield"
