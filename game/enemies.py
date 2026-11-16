import random
from dataclasses import dataclass


@dataclass
class Enemy:
    name: str
    emoji: str
    hp: int
    max_hp: int
    attack: int
    xp: int
    gold: int
    description: str

    def is_alive(self) -> bool:
        return self.hp > 0


def _goblin():
    return Enemy("Goblin", "👺", 12, 12, 6, 8, random.randint(3, 8),
                 "A sneaky little goblin with a rusty blade")

def _skeleton():
    return Enemy("Skeleton", "💀", 15, 15, 7, 10, random.randint(5, 10),
                 "Bones clatter as it lurches toward you")

def _orc():
    return Enemy("Orc Warrior", "👹", 22, 22, 10, 15, random.randint(8, 15),
                 "A brutish orc with a massive axe")

def _troll():
    return Enemy("Cave Troll", "🧌", 35, 35, 13, 25, random.randint(12, 20),
                 "A massive troll — wounds close before your eyes")

def _dragon():
    return Enemy("Ancient Dragon", "🐉", 60, 60, 18, 50, random.randint(30, 50),
                 "The dungeon's ultimate guardian. It breathes fire.")


_POOL_BY_FLOOR = {
    1: [_goblin, _skeleton],
    2: [_goblin, _skeleton, _orc],
    3: [_orc, _skeleton, _troll],
    4: [_orc, _troll],
    5: [_dragon],
}


def get_enemy_for_floor(floor: int) -> Enemy:
    factory = random.choice(_POOL_BY_FLOOR.get(floor, [_goblin]))
    return factory()
