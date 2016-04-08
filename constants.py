def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Const(object):
    @constant
    def PLACE_TAG():
        return "place"

    @constant
    def MONSTERS_TAG():
        return "enemie"

    @constant
    def NAME_TAG():
        return "name"

    @constant
    def LEVEL_TAG():
        return "level"

    @constant
    def DESCRIPTION_TAG():
        return "description"

    @constant
    def LOCATION_TAG():
        return "location"

    @constant
    def WEAPON_TAG():
        return "weapon"
