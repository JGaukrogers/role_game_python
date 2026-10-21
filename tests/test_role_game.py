import pytest

from src import Game

# To test, run:
# python -m pytest tests/test_role_game.py


# GO test
def test_basic_go_test():
    game = Game()
    game.load('games/DemoGame.xml')
    assert game.goto('sEa') == 'You go to sEa'


def test_not_place_test():
    game = Game()
    game.load('games/DemoGame.xml')
    assert game.goto('hell') == 'Cannot go to hell'


def test_not_connected_place_test():
    game = Game()
    game.load('games/DemoGame.xml')
    assert game.goto('town') == 'Cannot go to town'


# LOOK test


# places
@pytest.mark.parametrize(
    'place_name, expected_result',
    [
        ('forest', 'It is a nice forest.'),
        ('sea', 'You can see the sea from here'),
        ('town', 'Cannot look at town'),
    ],
)
def test_look_place_test(place_name: str, expected_result: str):
    game = Game()
    game.load('games/LookTest.xml')
    assert game.look_at(place_name) == expected_result


# enemies
def test_basic_look_enemy():
    game = Game()
    game.load('games/LookTest.xml')
    assert game.look_at('enemy1') == 'Description e1'


# items
@pytest.mark.parametrize(
    'object_name, expected_result',
    [
        ('sword', 'Just a lousy sword'),
        ('shield', 'Just a lousy shield'),
        ('amulet', 'Pretty amulet'),
    ],
)
def test_look_object_in_room(object_name: str, expected_result: str):
    game = Game()
    game.load('games/LookTest.xml')
    assert game.look_at('sword') == 'Just a lousy sword'


def test_look_object_in_backpack():
    game = Game()
    game.load('games/LookTest.xml')
    game.pickup('sword')
    assert game.look_at('sword') == 'Just a lousy sword'


@pytest.mark.parametrize(
    'object_name, expected_result',
    [
        ('sword', 'Just a lousy sword. You have it equipped'),
        ('shield', 'Just a lousy shield. You have it equipped'),
        ('amulet', 'Pretty amulet'),
    ],
)
def test_equip_item_and_look(object_name: str, expected_result: str):
    game = Game()
    game.load('games/LookTest.xml')
    game.pickup(object_name)
    game.equip_item(object_name)
    assert game.look_at(object_name) == expected_result


def test_look_object_switch_equipped_weapon():
    game = Game()
    game.load('games/LookTest.xml')
    game.pickup('sword')
    game.pickup('sword2')
    game.equip_item('sword')
    assert game.look_at('sword') == 'Just a lousy sword. You have it equipped'
    assert game.look_at('sword2') == 'Another sword'
    game.equip_item('sword2')
    assert game.look_at('sword') == 'Just a lousy sword'
    assert game.look_at('sword2') == 'Another sword. You have it equipped'


def test_look_nonexistent():
    game = Game()
    game.load('games/LookTest.xml')
    assert game.look_at('nonexistent') == 'Cannot look at nonexistent'


# PICKUP


def test_basic_pickup():
    game = Game()
    game.load('games/LookTest.xml')
    assert game.pickup('swoRd') == 'You just picked up a swoRd'


def test_already_picked_up():
    game = Game()
    game.load('games/LookTest.xml')
    game.pickup('sword')
    assert game.pickup('swoRd') == 'Cannot pickup swoRd'


def test_pick_up_from_alive_enemy():
    game = Game()
    game.load('games/LookTest.xml')
    assert game.pickup('ring') == 'Cannot pickup ring'


def test_pick_up_from_dead_enemy():
    game = Game()
    game.load('games/LookTest.xml')
    game.fight('Enemy1')
    assert game.pickup('ring') == 'You just picked up a ring'


def test_pick_up_nonexistent():
    game = Game()
    game.load('games/LookTest.xml')
    assert game.pickup('nonexistent') == 'Cannot pickup nonexistent'


# SEARCH


# places
def test_search_basic():
    game = Game()
    game.load('games/SearchTest.xml')
    assert game.search() == 'You found a sword\nYou found a amulet\nYou found a shield\n'


def test_search_place_full():
    game = Game()
    game.load('games/SearchTest.xml')
    assert game.search('Forest') == 'You found a sword\nYou found a amulet\nYou found a shield\n'


def test_search_empty_place():
    game = Game()
    game.load('games/SearchTest.xml')
    game.goto('sea')
    assert game.search() == 'Found nothing'


# enemies
def test_search_alive_enemy():
    game = Game()
    game.load('games/SearchTest.xml')
    assert game.search('Enemy1') == 'You cannot search Enemy1 while it is alive!'


@pytest.mark.parametrize(
    'enemy_name, expected_result',
    [
        ('Enemy1', 'You found a ring\n'),
        ('Enemy2', 'Found nothing in Enemy2'),
    ],
)
def test_search_dead_enemy(enemy_name: str, expected_result: str):
    game = Game()
    game.load('games/SearchTest.xml')
    game.fight(enemy_name)
    assert game.search(enemy_name) == expected_result


def test_search_backpack_full():
    game = Game()
    game.load('games/SearchTest.xml')
    game.pickup('sword')
    game.pickup('amulet')
    game.pickup('shield')
    message = 'You look in your backpack:\n\tYou have a sword\n\tYou have a amulet\n\tYou have a shield'
    assert game.search('backpack') == message


def test_search_backpack_empty():
    game = Game()
    game.load('games/SearchTest.xml')
    assert game.search('backpack') == 'You look in your backpack:'


def test_search_backpack_emptied():
    game = Game()
    game.load('games/SearchTest.xml')
    game.pickup('sword')
    game.equip_item('sword')
    assert game.search('backpack') == 'You look in your backpack:'


def test_search_nonexistent():
    game = Game()
    game.load('games/SearchTest.xml')
    assert game.search('nonexistent') == 'Cannot search nonexistent'


# EQUIP


@pytest.mark.parametrize(
    'item_name, expected_result',
    [
        ('sword+1', 'You equipped your sword+1'),
        ('shield+1', 'You equipped your shield+1'),
    ],
)
def test_equip_item(item_name: str, expected_result: str):
    game = Game()
    game.load('games/EquipTest.xml')
    game.pickup('sword+1')
    assert game.equip_item('sword+1') == 'You equipped your sword+1'


def test_reequip_weapon():
    game = Game()
    game.load('games/EquipTest.xml')
    game.pickup('sword+1')
    game.pickup('sword+2')
    game.equip_item('sword+1')
    assert game.equip_item('sword+2') == 'You equipped your sword+2'
    message = 'You look in your backpack:\n\tYou have a sword+1'
    assert game.search('backpack') == message


def test_reequip_shield():
    game = Game()
    game.load('games/EquipTest.xml')
    game.pickup('shield+1')
    game.pickup('shield+2')
    game.equip_item('shield+1')
    assert game.equip_item('shield+2') == 'You equipped your shield+2'
    message = 'You look in your backpack:\n\tYou have a shield+1'
    assert game.search('backpack') == message


def test_equip_equipped_weapon():
    game = Game()
    game.load('games/EquipTest.xml')
    game.pickup('sword+1')
    game.equip_item('sword+1')
    assert game.equip_item('sword+1') == 'sword+1 is already equipped'


def test_equip_equipped_shield():
    game = Game()
    game.load('games/EquipTest.xml')
    game.pickup('shield+1')
    game.equip_item('shield+1')
    assert game.equip_item('shield+1') == 'shield+1 is already equipped'


@pytest.mark.parametrize(
    'item_name, expected_result',
    [
        # We can't equip a nonexistent item
        ('nothing', 'You have no nothing to equip'),
        # We can't equip an item that exists butt we don't posess
        ('sword+3', 'You have no sword+3 to equip'),
    ],
)
def test_equip_fail(item_name: str, expected_result: str):
    game = Game()
    game.load('games/EquipTest.xml')
    assert game.equip_item(item_name) == expected_result


def test_cannot_equip():
    game = Game()
    game.load('games/EquipTest.xml')
    game.pickup('amulet')
    assert game.equip_item('amulet') == "You can't equip amulet"


# FIGHT


@pytest.mark.parametrize(
    'enemy_name, expected_result',
    [
        # We can fight against an existing enemy while in the same room
        ('enemy1', 'You just killed the enemy1'),
        # We can't fight against an existing enemy while located in a different room
        ('enemy3', 'There is no enemy3 to fight'),
        # We can't fight against a nonexisting enemy
        ('nonexistent', 'There is no nonexistent to fight'),
    ],
)
def test_fight_basic(enemy_name: str, expected_result: str):
    game = Game()
    game.load('games/FightTest.xml')
    assert game.fight(enemy_name) == expected_result


def test_fight_dead_enemy():
    game = Game()
    game.load('games/FightTest.xml')
    game.fight('enemy1')
    assert game.fight('enemy1') == 'enemy1 is already dead'
