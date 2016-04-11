class Place:

    def __init__(self, name, description, new_id, connections=None, objects=None):
        if connections is None:
            connections = []
        if objects is None:
            objects = []

        self.name = name
        self.description = description
        self.id = new_id
        self.connections_list = connections
        self.objects_list = objects

        # TODO: get possible objects
        self.enemies_list = []
        self.possiblePaths_list = []

    def to_string(self):
        string = self.id + ": " + self.name + ": " + self.description
        return string

    def add_path(self, place):
        self.possiblePaths_list.append(place)

    def add_enemy(self, enemy):
        self.enemies_list.append(enemy)

    def get_full_description(self):
        string = self.description
        for e in self.enemies_list:
            if e.is_alive:
                string += "\n" + "You see a " + e.name + ". " + e.description
            else:
                string += "\n" + "You see a dead " + e.name
        return string

    def __str__(self):
        string = self.id + ": " + self.name
        for p in self.possiblePaths_list:
            string += ": " + p.id
        return string
