from .items import Item, Shield, Weapon


class Character:
    name: str
    description: str
    is_alive: bool

    def kill(self) -> None:
        self.is_alive = False

    def __init__(self, name: str, description: str, alive: bool = True) -> None:
        self.name = name
        self.description = description
        # alive = false -> character is dead
        self.is_alive = alive


class Enemy(Character):
    level: int
    object_list: list[Item]

    def __init__(self, name: str, description: str, level: int, object_list: list[Item]) -> None:
        Character.__init__(self, name, description, True)
        self.level = level
        self.object_list = object_list


class Protagonist(Character):
    level: int
    location: list[Item] | None
    rucksack: list[Item]
    weaponInHand: Weapon|None
    shieldInHand: Shield|None

    def increase_level(self) -> None:
        self.level += 1

    def add_to_rucksack(self, obj: Item) -> None:
        self.rucksack.append(obj)

    def __init__(self, name: str, description: str) -> None:
        Character.__init__(self, name, description, True)
        self.level = 1
        self.location = None
        self.rucksack = []
        self.weaponInHand = None
        self.shieldInHand = None
