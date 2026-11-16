from game.player import Player


def test_take_damage_subtracts_defense():
    p = Player(name="Test", defense=3)
    actual = p.take_damage(8)
    assert actual == 5
    assert p.hp == 25


def test_take_damage_minimum_one():
    p = Player(name="Test", defense=100)
    actual = p.take_damage(5)
    assert actual == 1
    assert p.hp == 29


def test_heal_caps_at_max_hp():
    p = Player(name="Test", hp=20, max_hp=30)
    healed = p.heal(20)
    assert healed == 10
    assert p.hp == 30


def test_use_potion_heals_and_consumes():
    p = Player(name="Test", hp=10, max_hp=30, potions=2)
    healed = p.use_potion()
    assert healed == 15
    assert p.hp == 25
    assert p.potions == 1


def test_use_potion_no_potions_returns_zero():
    p = Player(name="Test", potions=0)
    assert p.use_potion() == 0


def test_gain_xp_triggers_level_up():
    p = Player(name="Test")
    leveled = p.gain_xp(20)
    assert leveled is True
    assert p.level == 2
    assert p.hp == p.max_hp


def test_gain_xp_no_level_up():
    p = Player(name="Test")
    leveled = p.gain_xp(5)
    assert leveled is False
    assert p.level == 1


def test_is_alive():
    p = Player(name="Test", hp=1)
    assert p.is_alive() is True
    p.hp = 0
    assert p.is_alive() is False
