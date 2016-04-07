#!/usr/bin/python3.4

from character import Character


class Enemy(Character):

    def get_level(self):
        return self.level

    def get_location(self):
        return self.location

    def to_string(self):
        return self.name

    def __init__(self, name, description, level, location):
        Character.__init__(self, name, description, True)
        self.level = level
        self.location = location
