# monster.py
# This file will contain the Monster class and related logic.

class Monster:
    """
    Represents an enemy monster in the game.
    """
    def __init__(self, name: str, hp: int, attack: int, defense: int, xp_reward: int):
        """
        Initializes a new monster.

        Args:
            name: The name of the monster.
            hp: The health points of the monster.
            attack: The attack power of the monster.
            defense: The defense power of the monster.
            xp_reward: The experience points awarded for defeating the monster.
        """
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward

    def is_alive(self) -> bool:
        """Checks if the monster is still alive."""
        return self.hp > 0

    def display_info(self):
        """Displays the monster's information."""
        print(f"--- {self.name} ---")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"ATK: {self.attack} | DEF: {self.defense}")
        print(f"--------------------")
