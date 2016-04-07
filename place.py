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
        self._id = new_id
        self.__connections_list = connections
        self.__objects_list = objects

        # TODO: get possible paths and objects
        self.__enemies_list = []
        self.__possiblePaths_list = []

    def to_string(self):
        string = self._id + ": " + self.__name + ": " + self.__description
        return string

    def get_id(self):
        return self._id

    def get_connection_ids(self):
        return self.__connections_list

    def add_path(self, place):
        self.__possiblePaths_list.append(place)

    def __str__(self):
        string = self._id + ": " + self.__name
        for p in self.__possiblePaths_list:
            string += ": " + p.get_id()
        return string
