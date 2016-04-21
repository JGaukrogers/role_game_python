import pytest

from role_game import Game


# To test, run:
# python3 -m pytest tests/test_role_game.py

# @pytest.mark.parametrize(
#     "data, expectation", [
#         ("a", b)
#     ]
# )


# GO test
def test_basic_go_test():
    game = Game()
    game.load("games/DemoGame.xml")
    assert game.goto("sEa") == "You go to sEa"


def test_not_place_test():
    game = Game()
    game.load("games/DemoGame.xml")
    assert game.goto("hell") == "Cannot go to hell"


def test_not_connected_place_test():
    game = Game()
    game.load("games/DemoGame.xml")
    assert game.goto("town") == "Cannot go to town"


# LOOK test


# places
def test_basic_look_place_test():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("forest") == "It is a nice forest."


def test_look_next_place_test():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("sea") == "You can see the sea from here"


def test_look_far_place_test():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("town") == "Cannot look at town"


# enemies
def test_basic_look_enemy():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("enemy1") == "Description e1"


# items
def test_look_object_at_floor():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("sword") == "Just a lousy sword"


def test_look_object_at_floor_weapon():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("sword") == "Just a lousy sword"


def test_look_object_at_floor_shield():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("shield") == "Just a lousy shield"


def test_look_object_at_floor_item():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("amulet") == "Pretty amulet"


def test_look_object_in_backpack():
    game = Game()
    game.load("games/LookTest.xml")
    game.pickup("sword")
    assert game.look_at("sword") == "Just a lousy sword"


def test_look_object_equipped_weapon():
    game = Game()
    game.load("games/LookTest.xml")
    game.pickup("sword")
    game.equip("sword")
    assert game.look_at("sword") == "Just a lousy sword. You have it equipped"


def test_look_object_equipped_shield():
    game = Game()
    game.load("games/LookTest.xml")
    game.pickup("shield")
    game.equip("shield")
    assert game.look_at("shield") == "Just a lousy shield. You have it equipped"


def test_look_object_not_equipped_amulet():
    game = Game()
    game.load("games/LookTest.xml")
    game.pickup("amulet")
    game.equip("amulet")
    assert game.look_at("amulet") == "Pretty amulet"


def test_look_object_switch_equipped_weapon():
    game = Game()
    game.load("games/LookTest.xml")
    game.pickup("sword")
    game.pickup("sword2")
    game.equip("sword")
    assert game.look_at("sword") == "Just a lousy sword. You have it equipped"
    assert game.look_at("sword2") == "Another sword"
    game.equip("sword2")
    assert game.look_at("sword") == "Just a lousy sword"
    assert game.look_at("sword2") == "Another sword. You have it equipped"


def test_look_nonexistent():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("nonexistent") == "Cannot look at nonexistent"


# PICKUP


def test_basic_pickup():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.pickup("swoRd") == "You just picked up a swoRd"


def test_already_picked_up():
    game = Game()
    game.load("games/LookTest.xml")
    game.pickup("sword")
    assert game.pickup("swoRd") == "Cannot pickup swoRd"


def test_pick_up_from_alive_enemy():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.pickup("ring") == "Cannot pickup ring"


def test_pick_up_from_dead_enemy():
    game = Game()
    game.load("games/LookTest.xml")
    game.fight("Enemy1")
    assert game.pickup("ring") == "You just picked up a ring"


def test_pick_up_nonexistent():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.pickup("nonexistent") == "Cannot pickup nonexistent"


# SEARCH


# places
def test_search_basic():
    game = Game()
    game.load("games/SearchTest.xml")
    message = "You found a sword\n" \
              + "You found a amulet\n" \
              + "You found a shield\n"
    assert game.search() == message


def test_search_place_full():
    game = Game()
    game.load("games/SearchTest.xml")
    message = "You found a sword\n" \
              + "You found a amulet\n" \
              + "You found a shield\n"
    assert game.search("Forest") == message


def test_search_place_empty():
    game = Game()
    game.load("games/SearchTest.xml")
    game.goto("sea")
    assert game.search() == "Found nothing"


# enemies
def test_search_alive_enemy():
    game = Game()
    game.load("games/SearchTest.xml")
    assert game.search("Enemy1") == "You cannot search Enemy1 while it is alive!"


def test_search_dead_enemy1():
    game = Game()
    game.load("games/SearchTest.xml")
    game.fight("Enemy1")
    assert game.search("Enemy1") == "You found a ring\n"


def test_search_dead_enemy2():
    game = Game()
    game.load("games/SearchTest.xml")
    game.fight("Enemy2")
    assert game.search("Enemy2") == "Found nothing in Enemy2"


def test_search_backpack_full():
    game = Game()
    game.load("games/SearchTest.xml")
    game.pickup("sword")
    game.pickup("amulet")
    game.pickup("shield")
    message = "You look in your backpack:" \
              + "\n\tYou have a sword" \
              + "\n\tYou have a amulet" \
              + "\n\tYou have a shield"
    assert game.search("backpack") == message


def test_search_backpack_empty():
    game = Game()
    game.load("games/SearchTest.xml")
    assert game.search("backpack") == "You look in your backpack:"


def test_search_backpack_emptied():
    game = Game()
    game.load("games/SearchTest.xml")
    game.pickup("sword")
    game.equip("sword")
    assert game.search("backpack") == "You look in your backpack:"


def test_search_nonexistent():
    game = Game()
    game.load("games/SearchTest.xml")
    assert game.search("nonexistent") == "Cannot search nonexistent"

# EQUIP


def test_equip_weapon():
    game = Game()
    game.load("games/EquipTest.xml")
    game.pickup("sword+1")
    assert game.equip("sword+1") == "You equipped your sword+1"


def test_equip_shield():
    game = Game()
    game.load("games/EquipTest.xml")
    game.pickup("shield+1")
    assert game.equip("shield+1") == "You equipped your shield+1"


def test_reequip_weapon():
    game = Game()
    game.load("games/EquipTest.xml")
    game.pickup("sword+1")
    game.pickup("sword+2")
    game.equip("sword+1")
    assert game.equip("sword+2") == "You equipped your sword+2"
    message = "You look in your backpack:" \
              + "\n\tYou have a sword+1"
    assert game.search("backpack") == message


def test_reequip_shield():
    game = Game()
    game.load("games/EquipTest.xml")
    game.pickup("shield+1")
    game.pickup("shield+2")
    game.equip("shield+1")
    assert game.equip("shield+2") == "You equipped your shield+2"
    message = "You look in your backpack:" \
              + "\n\tYou have a shield+1"
    assert game.search("backpack") == message


def test_equip_fail():
    game = Game()
    game.load("games/EquipTest.xml")
    assert game.equip("nothing") == "You have no nothing to equip"


def test_cannot_equip():
    game = Game()
    game.load("games/EquipTest.xml")
    game.pickup("amulet")
    assert game.equip("amulet") == "You can't equip amulet"


def test_equip_nothing():
    game = Game()
    game.load("games/EquipTest.xml")
    assert game.equip("sword+3") == "You have no sword+3 to equip"

# FIGHT
