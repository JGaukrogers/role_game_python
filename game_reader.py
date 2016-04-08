import xml.etree.ElementTree as ET

from constants import Const
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
            self.place_list.append(self.get_place(place))

        # Get all monsters
        for enemy in root.iter('enemy'):
            self.enemy_list.append(self.get_enemy(enemy))

    def get_place(self, place):
        place_name = place.find(self.CONST.NAME_TAG).text
        description = place.find(self.CONST.DESCRIPTION_TAG).text
        place_id = int(place.find('id').text)

        connection_list = []
        for connection in place.iter('connection'):
            aux = int(connection.text)
            connection_list.append(aux)
        p = Place(place_name, description, place_id, connection_list)
        return p

    def get_enemy(self, enemy):
        name = enemy.find(self.CONST.NAME_TAG).text
        description = enemy.find(self.CONST.DESCRIPTION_TAG).text
        level = int(enemy.find(self.CONST.LEVEL_TAG).text)
        location = int(enemy.find(self.CONST.LOCATION_TAG).text)
        return Enemy(name, description, level, location)

    def __init__(self):
        self.place_list = []
        self.enemy_list = []
        self.CONST = Const()
