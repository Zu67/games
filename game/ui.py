from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.text import Text
from rich.prompt import Prompt
from rich.rule import Rule
from rich.columns import Columns

console = Console()


def _bar(current: int, maximum: int, width: int = 20) -> str:
    ratio = current / maximum if maximum > 0 else 0
    filled = int(ratio * width)
    color = "green" if ratio > 0.5 else "yellow" if ratio > 0.25 else "red"
    return f"[{color}]{'█' * filled}[/{color}][dim]{'░' * (width - filled)}[/dim]"


def show_title():
    console.clear()
    t = Text(justify="center")
    t.append("\n")
    t.append("  ⚔️   D U N G E O N   D E L V E R   ⚔️  \n\n", style="bold yellow")
    t.append("  A roguelike adventure — five floors, one chance.\n", style="dim")
    console.print(Panel(t, box=box.DOUBLE_EDGE, style="yellow", padding=(1, 4)))
    console.print()


def prompt_name() -> str:
    return Prompt.ask("[bold cyan]Enter your hero's name[/bold cyan]")


def show_floor_intro(floor: int):
    console.clear()
    label = "THE DRAGON'S LAIR" if floor == 5 else f"FLOOR  {floor}  OF  5"
    style = "bold red" if floor == 5 else "bold yellow"
    console.print()
    console.print(Rule(f"[{style}]{label}[/{style}]", style="dim yellow"))
    console.print()
    input("  Press Enter to descend...\n")


def _player_panel(player) -> Panel:
    t = Table(box=None, show_header=False, padding=(0, 1))
    t.add_column(style="bold cyan", no_wrap=True)
    t.add_column()
    t.add_row("Hero", f"[bold]{player.name}[/bold]  Lv.{player.level}")
    t.add_row("HP", f"{_bar(player.hp, player.max_hp)} {player.hp}/{player.max_hp}")
    t.add_row("XP", f"{_bar(player.xp, player.xp_to_next, 15)} {player.xp}/{player.xp_to_next}")
    t.add_row("ATK / DEF", f"[red]{player.attack}[/red] / [blue]{player.defense}[/blue]")
    t.add_row("Gold", f"💰 {player.gold}")
    t.add_row("Potions", f"🧪 {player.potions}")
    return Panel(t, title="[bold]Stats[/bold]", box=box.ROUNDED, style="cyan")


def show_room(room, player):
    console.clear()
    room_panel = Panel(
        f"\n{room.description}\n",
        title=f"[bold yellow]{room.type.value.upper()}[/bold yellow]",
        box=box.HEAVY,
        style="yellow",
        padding=(1, 2),
    )
    console.print(Columns([_player_panel(player), room_panel], equal=True, expand=True))
    console.print()


def show_combat_screen(player, enemy):
    console.clear()
    enemy_panel = Panel(
        f"\n  {enemy.emoji}  {enemy.description}\n\n"
        f"  HP  {_bar(enemy.hp, enemy.max_hp)} {enemy.hp}/{enemy.max_hp}\n",
        title=f"[bold red]{enemy.name}[/bold red]",
        box=box.HEAVY,
        style="red",
        padding=(1, 2),
    )
    console.print(Columns([_player_panel(player), enemy_panel], equal=True, expand=True))
    console.print()


def show_combat_log(lines: list[str]):
    for line in lines:
        console.print(f"  {line}")
    console.print()


def prompt_combat(player) -> str:
    potion_str = f"[P]otion 🧪×{player.potions}" if player.potions > 0 else "[dim][P]otion 🧪×0[/dim]"
    console.print(f"  [bold][A]ttack[/bold]  ·  {potion_str}  ·  [bold][F]lee[/bold]")
    return Prompt.ask("  Choose", choices=["a", "p", "f"], default="a", show_choices=False).lower()


def show_treasure(kind: str, amount: int = 0):
    if kind == "potion":
        console.print(Panel("🧪 You find a [bold green]Health Potion[/bold green]! (+1 potion)", style="green"))
    else:
        console.print(Panel(f"💰 You pocket [bold yellow]{amount} gold[/bold yellow]!", style="yellow"))
    console.print()
    input("  Press Enter to continue...\n")


def show_rest(healed: int):
    msg = (f"💤 You rest and recover [bold green]{healed} HP[/bold green]."
           if healed > 0 else "💤 You rest, but your HP is already full.")
    console.print(Panel(msg, style="green"))
    console.print()
    input("  Press Enter to continue...\n")


def show_enemy_defeated(enemy, leveled: bool):
    msg = f"⚔️  You defeated the [bold]{enemy.name}[/bold]!\n  +{enemy.xp} XP  ·  +{enemy.gold} gold"
    if leveled:
        msg += "\n\n  [bold yellow]✨ LEVEL UP! ✨[/bold yellow]  ATK +3 · DEF +1 · HP fully restored"
    console.print(Panel(msg, style="green"))
    console.print()
    input("  Press Enter to continue...\n")


def show_stairs(floor: int):
    console.print(Panel(
        f"🪜 Floor {floor} cleared! The stairs descend into deeper darkness...",
        style="yellow",
    ))
    console.print()
    input("  Press Enter to descend...\n")


def show_game_over(player):
    console.clear()
    msg = (
        f"\n  💀  [bold red]YOU HAVE FALLEN[/bold red]  💀\n\n"
        f"  {player.name} perished in the dungeon.\n"
        f"  Gold collected : {player.gold}\n"
        f"  Level reached  : {player.level}\n"
    )
    console.print(Panel(msg, title="[bold red]GAME OVER[/bold red]", box=box.DOUBLE_EDGE, style="red"))
    console.print()


def show_victory(player):
    console.clear()
    msg = (
        f"\n  🏆  [bold yellow]VICTORY![/bold yellow]  🏆\n\n"
        f"  {player.name} has conquered the dungeon!\n\n"
        f"  Final Level  : {player.level}\n"
        f"  Gold Earned  : {player.gold}\n"
        f"  HP Remaining : {player.hp}/{player.max_hp}\n"
    )
    console.print(Panel(msg, title="[bold yellow]DUNGEON CLEARED[/bold yellow]", box=box.DOUBLE_EDGE, style="yellow"))
    console.print()
