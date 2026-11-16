from dataclasses import dataclass


@dataclass
class Player:
    name: str
    hp: int = 30
    max_hp: int = 30
    attack: int = 8
    defense: int = 3
    gold: int = 0
    level: int = 1
    xp: int = 0
    xp_to_next: int = 20
    potions: int = 2

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> int:
        actual = max(1, amount - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

    def heal(self, amount: int) -> int:
        before = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - before

    def use_potion(self) -> int:
        if self.potions <= 0:
            return 0
        self.potions -= 1
        return self.heal(15)

    def gain_xp(self, amount: int) -> bool:
        """Returns True if the player leveled up."""
        self.xp += amount
        if self.xp >= self.xp_to_next:
            self._level_up()
            return True
        return False

    def _level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next
        self.xp_to_next = int(self.xp_to_next * 1.6)
        self.max_hp += 10
        self.hp = self.max_hp
        self.attack += 3
        self.defense += 1
