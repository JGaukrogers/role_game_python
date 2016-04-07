#!/usr/bin/python3.4

import xml.etree.ElementTree as ET

from constants import _Const
from place import Place
from enemy import Enemy


class GameReader:

    # tree = ET.parse(path)
    # root = tree.getroot()
    # For testing purposes
    # for place in root.iter('place'):
        # print(place.find('name').text)

    def parse_game(self, file):
        tree = ET.parse(file)
        root = tree.getroot()

        # Get all places
        for place in root.iter('place'):
            self.__place_list.append(self.__get_place(place))

        # Get all monsters
        for enemy in root.iter('enemy'):
            self.__monster_list.append(self.__get_enemy(enemy))

    def __get_place(self, place):
        place_name = place.find(self.__CONST.NAME_TAG).text
        description = place.find(self.__CONST.DESCRIPTION_TAG).text
        place_id = int(place.find('id').text)

        connection_list = []
        for connection in place.iter('connection'):
            aux = int(connection.text)
            connection_list.append(aux)
        p = Place(place_name, description, place_id, connection_list)
        return p

    def __get_enemy(self, enemy):
        name = enemy.find(self.__CONST.NAME_TAG).text
        description = enemy.find(self.__CONST.DESCRIPTION_TAG).text
        level = int(enemy.find(self.__CONST.LEVEL_TAG).text)
        location = int(enemy.find(self.__CONST.LOCATION_TAG).text)
        return Enemy(name, description, level, location)

    def get_places_list(self):
        return self.__place_list

    def get_enemies_list(self):
        return self.__monster_list

    def __init__(self):
        self.__place_list = []
        self.__monster_list = []
        self.__CONST = _Const()
