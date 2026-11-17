# Games

## Dungeon Delver

A terminal roguelike. You pick a name, then descend five floors. Each floor is a shuffle of fights, treasure, and a place to rest. Floor 5 is a rest and then the dragon.

A blank name becomes Hero. You start at 30 HP, attack 8, defense 3, level 1, and 2 potions. The next level costs 20 XP.

Attack, drink a potion, or try to flee. Damage is your attack plus a roll from -2 to +3, and it never falls below 1. An incoming hit subtracts defense once, and it also never falls below 1. A potion heals 15 HP. A rest heals 15 HP and does not use a potion. Treasure is a potion 40% of the time. Otherwise it is gold equal to a roll from 5 to 20, multiplied by the floor. Winning a fight adds that enemy's XP and gold. A level-up adds 10 max HP, refills HP, adds 3 attack and 1 defense, and multiplies the XP required by 1.6.

Floor 1 is a goblin or a skeleton. Floor 2 adds an orc. Floor 3 is an orc, a skeleton, or a cave troll. Floor 4 is an orc or a cave troll. Floor 5's fight is the ancient dragon. Clearing floor 5 is the win.

```bash
pip install -r requirements.txt
python main.py
```

In a fight: `A` attack, `P` drink a potion, `F` flee (about a 50% chance).

```bash
pytest
```

The game code is `main.py` and `game/`. Tests are in `tests/`.
