from unittest.mock import patch

from game.player import Player
from game.enemies import Enemy
import game.combat as combat


def _enemy(**kwargs):
    defaults = dict(name="Goblin", emoji="👺", hp=12, max_hp=12, attack=6, xp=8, gold=5, description="test")
    return Enemy(**{**defaults, **kwargs})


def test_player_damage_minimum_one():
    p = Player(name="Test", attack=1)
    with patch("game.combat.random.randint", return_value=-2):
        dmg = combat.player_damage(p)
    assert dmg == 1


def test_player_damage_uses_attack_stat():
    p = Player(name="Test", attack=10)
    with patch("game.combat.random.randint", return_value=0):
        dmg = combat.player_damage(p)
    assert dmg == 10


def test_enemy_damage_reduced_by_defense():
    p = Player(name="Test", defense=4)
    e = _enemy(attack=10)
    with patch("game.combat.random.randint", return_value=0):
        dmg = combat.enemy_damage(e, p)
    assert dmg == 6


def test_enemy_damage_minimum_one():
    p = Player(name="Test", defense=100)
    e = _enemy(attack=5)
    with patch("game.combat.random.randint", return_value=0):
        dmg = combat.enemy_damage(e, p)
    assert dmg == 1
