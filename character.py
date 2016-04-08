class Character:

    def kill(self):
        self.is_alive = False

    def __init__(self, name, description, alive=True):
        self.name = name
        self.description = description
        # alive = false -> character is dead
        self.is_alive = alive
