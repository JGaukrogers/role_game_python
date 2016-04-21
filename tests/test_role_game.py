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


def test_look_object_at_floor_sword():
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


def test_look_nonexistent():
    game = Game()
    game.load("games/LookTest.xml")
    assert game.look_at("nonexistent") == "Cannot look at nonexistent"


# PICKUP

# SEARCH

# EQUIP

# FIGHT