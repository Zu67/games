import random

from game.player import Player
from game.enemies import Enemy


def player_damage(player: Player) -> int:
    """Damage the player deals to an enemy (no enemy defense in this game)."""
    return max(1, player.attack + random.randint(-2, 3))


def enemy_damage(enemy: Enemy, player: Player) -> int:
    """Damage an enemy deals to the player after applying player defense."""
    raw = enemy.attack + random.randint(-2, 3)
    return max(1, raw - player.defense)
