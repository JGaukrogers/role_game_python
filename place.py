#!/usr/bin/python3.4


class Place:
    # __name
    # __id
    # __description
    # __enemies_list = []
    # __possiblePaths_list = []
    # __connections_list = []
    # __objects_list = []

    def __init__(self, name, description, new_id, connections=[], objects=[]):
        self.__name = name
        self.__description = description
        self.__id = new_id
        self.__connections_list = connections
        self.__objects_list = objects

        # TODO: get possible objects
        self.__enemies_list = []
        self.__possiblePaths_list = []

    def to_string(self):
        string = self.__id + ": " + self.__name + ": " + self.__description
        return string

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_paths(self):
        return self.__possiblePaths_list

    def get_enemies(self):
        return self.__enemies_list

    def get_connection_ids(self):
        return self.__connections_list

    def add_path(self, place):
        self.__possiblePaths_list.append(place)

    def add_enemy(self, enemy):
        self.__enemies_list.append(enemy)

    def get_description(self):
        return self.__description

    def get_full_description(self):
        string = self.__description
        for e in self.__enemies_list:
            if e.is_alive():
                string += "\n" + "You see a " + e.get_name() + ". " + e.get_description()
            else:
                string += "\n" + "You see a dead " + e.get_name()
        return string

    def __str__(self):
        string = self.__id + ": " + self.__name
        for p in self.__possiblePaths_list:
            string += ": " + p.get_id()
        return string
