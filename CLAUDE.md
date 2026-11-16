# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project: Dungeon Delver

A terminal roguelike RPG with Rich UI. The player descends five floors of a dungeon, fights enemies in turn-based combat, collects loot, and levels up. Floor 5 ends with a boss dragon fight.

## Commands

```powershell
# Install dependencies
pip install -r requirements.txt

# Play the game
python main.py

# Run all tests
pytest

# Run a single test file
pytest tests/test_player.py -v

# Run a single test by name
pytest tests/test_combat.py::test_enemy_damage_reduced_by_defense -v
```

## Architecture

```
main.py          — game loop: run_combat(), handle_room(), main()
game/
  player.py      — Player dataclass (stats, heal, xp/leveling, potions)
  enemies.py     — Enemy dataclass + per-floor factory functions
  combat.py      — Damage calculations: player_damage(), enemy_damage()
  dungeon.py     — Room/RoomType, generate_floor() builds a shuffled room list
  ui.py          — All Rich display logic (panels, bars, prompts); never mutates state
tests/
  test_player.py — Unit tests for Player
  test_combat.py — Unit tests for combat damage with mocked random
```

### Key design decisions

- `ui.py` is purely presentational — it reads state but never modifies it. All state changes happen in `main.py` or on the model objects.
- `combat.py` only computes damage values; the caller in `main.py` applies them to `.hp`. This keeps the math testable without side effects.
- `generate_floor(floor)` returns a list of `Room` objects with types drawn from a shuffled pool. Floor 5 is hardcoded to `[REST, BOSS]`.
- Enemies are created fresh per combat via factory functions in `enemies.py`; `get_enemy_for_floor(floor)` picks randomly from the floor's pool.

### Extension points

- **New enemy types**: add a factory function in `enemies.py` and register it in `_POOL_BY_FLOOR`.
- **New room types**: add a value to `RoomType`, a description list in `_DESCRIPTIONS`, and a handler branch in `handle_room()` in `main.py`.
- **New items / inventory**: extend the `Player` dataclass and wire up new actions in `prompt_combat()` / the combat loop.
- **Persistence / save files**: `Player` is a plain dataclass — `dataclasses.asdict()` + `json.dump()` is a natural save format.

## Claude Code Feature Walkthrough

This repo is intentionally small enough to understand quickly and rich enough to demonstrate real Claude Code capabilities.

### Inline Editing
Ask Claude to extend the game: "add a poison status effect to the Troll" or "add a shop room type between floors." Claude will read the relevant files, make consistent changes across modules, and verify nothing breaks.

### Multi-file Refactoring
Try: "split `main.py` — move `run_combat` into `game/combat.py`." Claude will move code, fix imports, and keep tests green.

### Shell Commands
Claude can run `python main.py`, `pytest`, or `pip install` directly via the Bash/PowerShell tools and show you the output.

### Web Search & Fetch
Try: "look up the Rich `Layout` docs and add a split-screen layout to the combat view."

### Memory System
Claude maintains persistent memory at `~/.claude/projects/.../memory/`. Say "remember that I prefer enemy names in title case" and it will apply that preference in future sessions.

### Hooks (Automated Behaviors)
Hooks in `.claude/settings.json` run shell commands on Claude Code events. Try: "after every file edit, run pytest and show me the result."

### Plan Mode (`/plan`)
Before large changes like adding a save/load system, ask Claude to enter Plan Mode. It will lay out every file it intends to touch before writing a single line.

### Scheduled Agents
Use the `schedule` skill: "every day at 9am, check if the tests still pass and notify me."

### MCP Servers
Claude Code supports Model Context Protocol for external integrations. Configure them in settings under `mcpServers` — e.g., a filesystem server, database connector, or Slack integration.

### Subagents & Parallel Work
Claude can spawn specialized subagents in parallel. Try: "in parallel, find all places that modify `player.hp` directly and check if any bypass the defense calculation."
