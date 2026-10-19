from .character import Enemy
from .items import Item


class Place:
    name: str
    description: str
    id: int
    connections_list: list[int]
    objects_list: list[Item]
    enemies_list: list[Enemy]
    possiblePaths_list: list

    def __init__(
            self,
            name: str,
            description: str,
            new_id: int,
            connections: list[int] | None = None,
            objects: list[Item] | None = None,
            enemies: list[Enemy] | None = None,
    ) -> None:
        if connections is None:
            connections = []
        if objects is None:
            objects = []
        if enemies is None:
            enemies = []

        self.name = name
        self.description = description
        self.id = new_id
        self.connections_list = connections
        self.objects_list = objects
        self.enemies_list = enemies
        self.possiblePaths_list = []

    def to_string(self) -> str:
        return f'{self.id}: {self.name} {self.description}'

    def add_path(self, place: Place) -> None:
        self.possiblePaths_list.append(place)

    def add_enemy(self, enemy: Enemy) -> None:
        self.enemies_list.append(enemy)

    def get_full_description(self) -> str:
        string = self.description
        for e in self.enemies_list:
            if e.is_alive:
                string += f'\nYou see a {e.name}. {e.description}'
            else:
                string += f'\nYou see a dead {e.name}'
        return string

    def __str__(self) -> str:
        string = f'{self.id}: {self.name}'
        for p in self.possiblePaths_list:
            string += ': ' + p.id
        return string
