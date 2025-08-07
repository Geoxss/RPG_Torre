# character.py
# This file will contain the character creation and class logic.

class Player:
    """
    Represents the player character in the game.
    """
    def __init__(self, name: str):
        """
        Initializes a new player character.

        Args:
            name: The name of the character.
        """
        self.name = name
        self.level = 1
        self.exp = 0
        self.job_class = "Novice"

        # Base stats
        self.stats = {
            "str": 5,
            "agi": 5,
            "vit": 5,
            "int": 5,
            "dex": 5,
            "luk": 5
        }

        # Derived stats
        self.max_hp = self._calculate_max_hp()
        self.hp = self.max_hp
        self.max_sp = self._calculate_max_sp()
        self.sp = self.max_sp

    def _calculate_max_hp(self) -> int:
        """Calculates max HP based on vitality."""
        return 50 + self.stats["vit"] * 10

    def _calculate_max_sp(self) -> int:
        """Calculates max SP based on intelligence."""
        return 10 + self.stats["int"] * 5

    def display_sheet(self):
        """Displays the character sheet."""
        print(f"--- Character Sheet ---")
        print(f"Name: {self.name}")
        print(f"Class: {self.job_class}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"SP: {self.sp}/{self.max_sp}")
        print(f"--- Stats ---")
        for stat, value in self.stats.items():
            print(f"{stat.upper()}: {value}")
        print(f"-----------------------")
