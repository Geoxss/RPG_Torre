# monster.py
# This file will contain the Monster class and monster templates.

MONSTER_TEMPLATES = {
    "Poring": {
        "hp": 30,
        "attack": 8,
        "defense": 2,
        "xp_reward": 15
    },
    "Fabre": {
        "hp": 45,
        "attack": 12,
        "defense": 4,
        "xp_reward": 25
    },
    "Lunatic": {
        "hp": 40,
        "attack": 15,
        "defense": 3,
        "xp_reward": 30
    },
    "Hornet": {
        "hp": 60,
        "attack": 18,
        "defense": 5,
        "xp_reward": 50
    },
}

class Monster:
    """
    Represents an enemy monster in the game, created from a template.
    """
    def __init__(self, name: str):
        """
        Initializes a new monster from a template.

        Args:
            name: The name of the monster, must exist in MONSTER_TEMPLATES.
        """
        template = MONSTER_TEMPLATES.get(name)
        if not template:
            raise ValueError(f"Unknown monster template: {name}")

        self.name = name
        self.max_hp = template["hp"]
        self.hp = self.max_hp
        self.attack = template["attack"]
        self.defense = template["defense"]
        self.xp_reward = template["xp_reward"]

    def is_alive(self) -> bool:
        """Checks if the monster is still alive."""
        return self.hp > 0

    def display_info(self):
        """Displays the monster's information."""
        print(f"--- {self.name} ---")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"ATK: {self.attack} | DEF: {self.defense}")
        print(f"--------------------")
