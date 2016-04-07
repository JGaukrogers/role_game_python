#!/usr/bin/python3.4

from character import Character


class Protagonist(Character):

    def set_level(self, new_level):
        self.level = new_level

    def get_level(self):
        return self.level

    def increase_level(self):
        self.level += 1

    def set_location(self, new_location):
        self.location = new_location

    def get_location(self):
        return self.location

    def get_rucksack(self):
        return self.rucksack

    def add_to_rucksack(self, obj):
        self.rucksack.append(obj)

    def is_weapon_equipped(self):
        return self.weaponInHand is not None

    def is_shield_equipped(self):
        return self.shieldInHand is not None

    def __init__(self, name, description):
        Character.__init__(self, name, description, True)
        self.level = 1
        self.location = None
        self.rucksack = []
        self.weaponInHand = None
        self.shieldInHand = None
