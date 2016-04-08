#!/usr/bin/python3.4

from character import Character


class Protagonist(Character):

    def increase_level(self):
        self.level += 1

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
