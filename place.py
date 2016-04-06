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

        # TODO: get possible paths and objects
        self.__enemies_list = []
        self.__possiblePaths_list = []

    def to_string(self):
        string = self.__id + ": " + self.__name + ": " + self.__description
        return string
