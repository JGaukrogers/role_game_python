class Character:

    def is_alive(self):
        return self.alive

    def kill(self):
        self.alive = False

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def __init__(self, name, description, alive=True):
        self.name = name
        self.description = description
        # alive = false -> character is dead
        self.alive = alive
