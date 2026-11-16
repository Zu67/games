import random
from dataclasses import dataclass
from enum import Enum


class RoomType(Enum):
    COMBAT = "combat"
    TREASURE = "treasure"
    REST = "rest"
    BOSS = "boss"


@dataclass
class Room:
    type: RoomType
    floor: int
    description: str


_DESCRIPTIONS = {
    RoomType.COMBAT: [
        "Torchlight flickers across crude weapon racks lining the walls.",
        "The stench of blood and decay hits you as you enter.",
        "Bones crunch beneath your boots in this grim chamber.",
        "Crude carvings of monsters mark the damp stone walls.",
    ],
    RoomType.TREASURE: [
        "A dusty chest sits enticingly in the center of the room.",
        "Something glints in the rubble near the far wall.",
        "A skeleton slumps over a small pile of valuables.",
    ],
    RoomType.REST: [
        "A surprisingly cozy alcove with a bedroll and a fresh torch.",
        "A shrine radiates warmth — your wounds begin to close.",
        "Clear water trickles from a crack in the wall.",
    ],
    RoomType.BOSS: [
        "The ground trembles as you step into this vast, echoing chamber.",
    ],
}


def generate_floor(floor: int) -> list[Room]:
    if floor == 5:
        return [
            Room(RoomType.REST, floor, random.choice(_DESCRIPTIONS[RoomType.REST])),
            Room(RoomType.BOSS, floor, _DESCRIPTIONS[RoomType.BOSS][0]),
        ]

    pool = [RoomType.COMBAT, RoomType.COMBAT, RoomType.TREASURE, RoomType.REST, RoomType.COMBAT]
    random.shuffle(pool)
    return [Room(t, floor, random.choice(_DESCRIPTIONS[t])) for t in pool]
