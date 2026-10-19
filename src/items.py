class Item:

    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __name__(self) -> str:
        return 'Item'


class Weapon (Item):

    attack: int

    def __init__(self, name: str, description: str, attack: int) -> None:
        Item.__init__(self, name, description)
        self.attack = attack

    def __name__(self) -> str:
        return 'Weapon'


class Shield(Item):

    defense: int

    def __init__(self, name: str, description: str, defense: int) -> None:
        Item.__init__(self, name, description)
        self.defense = defense

    def __name__(self) -> str:
            return 'Shield'
