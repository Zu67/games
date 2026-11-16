# Dungeon Delver

A terminal roguelike. You pick a name, then descend five floors. Each floor is a shuffle of fights, treasure, and a place to rest. Floor 5 is a rest and then the dragon.

Attack, drink a potion, or try to flee. Damage is your attack plus a small random swing. Incoming hits are reduced by defense, and never drop below 1. Potions heal 15 HP. Experience levels you up, which raises max HP, attack, and defense.

## Play

```bash
pip install -r requirements.txt
python main.py
```

In a fight:

- `A` attack
- `P` drink a potion
- `F` flee (about a 50% chance)

## Tests

```bash
pytest
```

## What this is

This is the Dungeon Delver project from `Desktop/claude-code-demo`. It was not in a Git repository. The other desktop folders were left where they are: work trees such as the Lovelytics `advance_program` repo and the R1 / Cigna / Databricks projects, plus personal files (tax, budgets, lab reports).

A separate city-population guessing game exists only as a Google AI Studio prompt from November 2025. The generated source was not saved as files, so it is not in this project.
