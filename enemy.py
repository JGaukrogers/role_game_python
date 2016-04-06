#!/usr/bin/python3.4

from character import Character


# private int level;
# private int location;
# private ArrayList<Obj> drops;
#
# public Monster(String newName, String newDescription, int newLevel, int newLocation){
# 	name = newName;
# 	description = newDescription;
# 	level = newLevel;
# 	location = newLocation;
# 	alive = true;
# 	drops = new ArrayList<Obj>();
# }
#
# public int getLevel(){
# 	return level;
# }
#
# public int getLocation(){
# 	return location;
# }
#
# public String toString(){
# 	return name;
# }

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
