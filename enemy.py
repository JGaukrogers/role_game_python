from character import Character


class Enemy(Character):

    def __init__(self, name, description, level, location):
        Character.__init__(self, name, description, True)
        self.level = level
        self.location = location
