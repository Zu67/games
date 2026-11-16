"""Dungeon Delver — a terminal roguelike. Five floors, one life."""

import random
import sys

from game.player import Player
from game.enemies import get_enemy_for_floor
from game.dungeon import generate_floor, RoomType
import game.combat as combat
import game.ui as ui


def run_combat(player: Player, floor: int) -> str:
    """Returns 'win', 'lose', or 'flee'."""
    enemy = get_enemy_for_floor(floor)

    while player.is_alive() and enemy.is_alive():
        ui.show_combat_screen(player, enemy)
        action = ui.prompt_combat(player)

        log = []

        if action == "a":
            dmg = combat.player_damage(player)
            enemy.hp = max(0, enemy.hp - dmg)
            log.append(f"⚔️  You strike [bold]{enemy.name}[/bold] for [bold red]{dmg}[/bold red] damage!")

        elif action == "p":
            healed = player.use_potion()
            if healed > 0:
                log.append(f"🧪 You drink a potion and recover [bold green]{healed}[/bold green] HP!")
            else:
                log.append("[yellow]You have no potions left![/yellow]")

        elif action == "f":
            if random.random() < 0.5:
                log.append("💨 You slip back through the doorway!")
                ui.show_combat_log(log)
                return "flee"
            else:
                log.append("[yellow]Your escape route is cut off![/yellow]")

        if enemy.is_alive() and player.is_alive():
            dmg = combat.enemy_damage(enemy, player)
            player.hp = max(0, player.hp - dmg)
            log.append(f"💥 [bold]{enemy.name}[/bold] strikes you for [bold red]{dmg}[/bold red] damage!")

        ui.show_combat_log(log)

        if not player.is_alive():
            return "lose"
        if not enemy.is_alive():
            leveled = player.gain_xp(enemy.xp)
            player.gold += enemy.gold
            ui.show_enemy_defeated(enemy, leveled)
            return "win"

        input("  Press Enter to continue...\n")

    return "win" if player.is_alive() else "lose"


def handle_room(player: Player, room, floor: int) -> bool:
    """Returns False if the player dies."""
    ui.show_room(room, player)

    if room.type in (RoomType.COMBAT, RoomType.BOSS):
        result = run_combat(player, floor)
        if result == "lose":
            ui.show_game_over(player)
            return False

    elif room.type == RoomType.TREASURE:
        input("  You cautiously approach... Press Enter.\n")
        if random.random() < 0.4:
            player.potions += 1
            ui.show_treasure("potion")
        else:
            gold = random.randint(5, 20) * floor
            player.gold += gold
            ui.show_treasure("gold", gold)

    elif room.type == RoomType.REST:
        input("  You take a moment to rest... Press Enter.\n")
        healed = player.heal(15)
        ui.show_rest(healed)

    return True


def main():
    ui.show_title()
    name = ui.prompt_name().strip() or "Hero"
    player = Player(name=name)

    for floor in range(1, 6):
        ui.show_floor_intro(floor)
        for room in generate_floor(floor):
            if not handle_room(player, room, floor):
                return
        if floor < 5:
            ui.show_stairs(floor)

    ui.show_victory(player)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nFarewell, adventurer.")
        sys.exit(0)
