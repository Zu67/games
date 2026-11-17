# Games

## Dungeon Delver

This repository is Dungeon Delver, a terminal roguelike. It does not contain Headcount or a five-city population game. You pick a name, then descend five floors. Floors 1 through 4 are three fights, one treasure room, and one rest, in a random order. Floor 5 is a rest and then the dragon.

The name is stripped, so a blank name, including spaces only, becomes Hero. You start at 30 HP, attack 8, defense 3, level 1, 0 gold, and 2 potions. The next level costs 20 XP.

Your hit is attack plus a roll from -2 to +3, and it never falls below 1. An enemy hit is that enemy's attack plus the same roll, then defense is subtracted once, and it also never falls below 1. A potion heals 15 HP, up to your maximum. At full HP the potion is still used, the heal is 0, and the message says you have no potions left. A rest heals 15 HP and does not use a potion. Treasure is a potion 40% of the time. Otherwise it is gold equal to a roll from 5 to 20, multiplied by the floor. Winning a fight adds that enemy's XP and gold. A fight calls `gain_xp` once, so it can raise your level only once. Leftover XP stays, and the next level costs the old requirement times 1.6, rounded down. That leftover can already meet the new requirement. A dragon's 50 XP added to 19 XP leaves 49 toward a requirement of 32, and the next `gain_xp` call levels you again, including a call that adds 0. A level-up adds 10 max HP, refills HP, and adds 3 attack and 1 defense.

| Enemy | Floors | HP | Attack | XP | Gold |
| --- | --- | --- | --- | --- | --- |
| Goblin | 1, 2 | 12 | 6 | 8 | 3–8 |
| Skeleton | 1, 2, 3 | 15 | 7 | 10 | 5–10 |
| Orc Warrior | 2, 3, 4 | 22 | 10 | 15 | 8–15 |
| Cave Troll | 3, 4 | 35 | 13 | 25 | 12–20 |
| Ancient Dragon | 5 | 60 | 18 | 50 | 30–50 |

The Cave Troll's description says "wounds close before your eyes". Its HP does not regenerate. An unknown floor number would draw a Goblin. The game only asks for floors 1 through 5.

Fleeing a fight, including the dragon, does not end the run. The next room still happens. Leaving floor 5, even by fleeing the dragon, is the win. The title still says "A roguelike adventure — five floors, one chance." Floors 1 through 4 are headed "FLOOR  n  OF  5", with two spaces around the number and around OF. Floor 5 is headed "THE DRAGON'S LAIR". After floors 1 through 4 the game also says "Floor n cleared! The stairs descend into deeper darkness..." and waits on "Press Enter to descend..." again. Floor 5 does not show that stairs panel. The name prompt says "Enter your hero's name". Every floor, including the first and the dragon's lair, then waits on "Press Enter to descend...". The stats panel is titled "Stats" and its first row is labeled "Hero" even when the name is not Hero. A room panel is titled with the room type in uppercase: COMBAT, TREASURE, REST, or BOSS. The HP bar is 20 characters. It is green above half, yellow above a quarter and at exactly half, and red at a quarter or below. The filled length is the ratio times the width, rounded down. The XP bar is 15 characters and uses the same colors. Ctrl+C prints "Farewell, adventurer." and exits 0. Ctrl+D raises `EOFError`, which is not caught, so that farewell line is not printed. `Player.take_damage` subtracts defense again and is not called by the fight. The fight subtracts defense once, inside `enemy_damage`, then reduces HP by that amount.

```bash
pip install -r requirements.txt
python main.py
```

In a fight the prompt's choices are lowercase `a`, `p`, and `f`. The screen prints [A]ttack, [P]otion, and [F]lee. The potion label includes the count. At 0 it is dimmed and still accepted. Any other letter is rejected and the prompt repeats. Pressing Enter attacks, because the default is `a`. A flee succeeds when the draw is below 0.5, and then the enemy does not hit. A failed flee, an empty potion, and a potion drunk at full HP all still take the enemy's hit. A successful flee does not award XP or gold. At full HP a rest says "You rest, but your HP is already full." The level-up panel says "ATK +3 · DEF +1 · HP fully restored" and does not mention the +10 max HP. Death is titled "GAME OVER" and says "YOU HAVE FALLEN", with gold and level. The win is titled "DUNGEON CLEARED" and shows level, gold, and HP remaining.

```bash
pytest
```

The game code is `main.py` and `game/`. Tests are in `tests/`. They never import `main.py`, so they do not run a fight, a flee, or a room. `test_take_damage_subtracts_defense` expects `take_damage(8)` with defense 3 to return 5 and leave 25 HP. `test_take_damage_minimum_one` expects `take_damage(5)` with defense 100 to return 1 and leave 29 HP. `test_gain_xp_triggers_level_up` checks that `gain_xp(20)` returns true, the level is 2, and HP equals max HP. It does not check that max HP is 40, attack is 11, or defense is 4. The combat tests patch `random.randint` and check only `player_damage` and `enemy_damage`. `test_use_potion_no_potions_returns_zero` checks only that the return value is 0. It does not check HP or that the potion count stays 0. `test_gain_xp_no_level_up` checks that the level stays 1 and does not check that XP is 5. `test_is_alive` sets HP to 0 by assignment. It does not call `take_damage`. `test_heal_caps_at_max_hp` starts at 20 HP with a maximum of 30, calls `heal(20)`, and expects 10 HP healed and 30 HP remaining. No test checks that one `gain_xp` call levels only once.
