import xml.etree.ElementTree as ET
from enum import Enum

from .character import Enemy
from .items import Item, Shield, Weapon
from .place import Place


class TagType(Enum):
    PLACE = 'place'
    MONSTERS = 'enemy'
    NAME = 'name'
    LEVEL = 'level'
    DESCRIPTION = 'description'
    LOCATION = 'location'
    WEAPON = 'weapon'
    ID = 'id'


class GameReader:
    place_list: list[Place]
    enemy_list: list[Enemy]

    def __init__(self) -> None:
        self.place_list = []
        self.enemy_list = []

    def parse_game(self, file: str) -> None:
        tree = ET.parse(file)
        root = tree.getroot()

        # Get all places
        for place in root.iter('place'):
            self.place_list.append(self.get_place(place))

    def get_place(self, place: ET.Element[str]) -> Place:
        place_name = place.find(TagType.NAME.value).text
        description = place.find(TagType.DESCRIPTION.value).text
        place_id = int(place.find(TagType.ID.value).text)

        connection_list = []
        for connection in place.iter('connection'):
            aux = int(connection.text)
            connection_list.append(aux)

        objects = place.find('objects')
        object_list = self.get_objects(objects) if objects is not None else []
        enemy_list = []
        for enemy in place.iter('enemy'):
            enemy_list.append(self.get_enemy(enemy))

        return Place(place_name, description, place_id, connection_list, object_list, enemy_list)

    @staticmethod
    def get_objects(place: ET.Element[str]) -> list[Item]:
        object_list = []
        for obj in place.iter('weapon'):
            attributes = obj.attrib
            name = attributes['name']
            description = attributes['description']
            attack = int(attributes['attack'])
            object_list.append(Weapon(name, description, attack))
        for obj in place.iter('object'):
            attributes = obj.attrib
            name = attributes['name']
            description = attributes['description']
            object_list.append(Item(name, description))
        for obj in place.iter('shield'):
            attributes = obj.attrib
            name = attributes['name']
            description = attributes['description']
            defense = int(attributes['defense'])
            object_list.append(Shield(name, description, defense))
        return object_list

    def get_enemy(self, enemy: ET.Element[str]) -> Enemy:
        name = enemy.find(TagType.NAME.value).text
        description = enemy.find(TagType.DESCRIPTION.value).text
        level = int(enemy.find(TagType.LEVEL.value).text)
        # location = int(enemy.find(self.CONST.LOCATION_TAG).text)
        object_list = self.get_objects(enemy)
        return Enemy(name, description, level, object_list)
