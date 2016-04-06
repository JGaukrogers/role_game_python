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
            self.__place_list.append(self.get_place(place))

        # Get all monsters
        for enemy in root.iter('enemy'):
            self.__monster_list.append(self.get_enemy(enemy))

    def get_place(self, place):
        place_name = place.find(self.__CONST.NAME_TAG).text
        description = place.find(self.__CONST.DESCRIPTION_TAG).text
        place_id = place.find('id').text
        p = Place(place_name, description, place_id)
        return p

    def get_enemy(self, enemy):
        name = enemy.find(self.__CONST.NAME_TAG).text
        description = enemy.find(self.__CONST.DESCRIPTION_TAG).text
        level = enemy.find(self.__CONST.LEVEL_TAG).text
        location = enemy.find(self.__CONST.LOCATION_TAG).text
        return Enemy(name, description, level, location)

    def __init__(self):
        self.__place_list = []
        self.__monster_list = []
        self.__CONST = _Const()
