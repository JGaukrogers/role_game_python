import pytest

# To test, run:
# python3 -m pytest tests/test_protagonist.py

from protagonist import Protagonist
# from objects import Weapon, Shield


# def test_shield_is_equipped():
#     protagonist = Protagonist("name", "description")
#     shield = Shield("name", "description", 1)
#     protagonist.shieldInHand = shield
#     assert protagonist.is_shield_equipped() == True
#
#
# def test_shield_is_not_equipped():
#     protagonist = Protagonist("name", "description")
#     assert protagonist.is_shield_equipped() == False
#
#
# def test_weapon_is_equipped():
#     protagonist = Protagonist("name", "description")
#     weapon = Weapon("name", "description", 1)
#     protagonist.weaponInHand = weapon
#     assert protagonist.is_weapon_equipped() == True
#
#
# def test_weapon_is_not_equipped():
#     protagonist = Protagonist("name", "description")
#     assert protagonist.is_weapon_equipped() == False


def test_increase_level():
    protagonist = Protagonist("name", "description")
    protagonist.increase_level()
    assert protagonist.level == 2
