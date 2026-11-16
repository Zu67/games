# Games

## Dungeon Delver

A terminal roguelike. You pick a name, then descend five floors. Each floor is a shuffle of fights, treasure, and a place to rest. Floor 5 is a rest and then the dragon.

Attack, drink a potion, or try to flee. Damage is your attack plus a small random swing. Incoming hits are reduced by defense, and never drop below 1. Potions heal 15 HP. Experience levels you up, which raises max HP, attack, and defense.

```bash
pip install -r requirements.txt
python main.py
```

In a fight: `A` attack, `P` drink a potion, `F` flee (about a 50% chance).

```bash
pytest
```

The game code is `main.py` and `game/`. Tests are in `tests/`.
