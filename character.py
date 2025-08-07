# character.py
# This file will contain the character creation and class logic.

from jobs import JOB_CLASSES
from skills import SKILLS


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
        self.skills = []
        self.exp_to_next_level = self._calculate_exp_to_next_level()

        # Base stats
        self.stats = {
            "str": 1, "agi": 1, "vit": 1,
            "int": 1, "dex": 1, "luk": 1
        }

        # Derived stats are calculated after initialization
        self.max_hp = 0; self.hp = 0
        self.max_sp = 0; self.sp = 0
        self.attack = 0; self.defense = 0; self.magic_attack = 0
        self._recalculate_derived_stats()

    def _recalculate_derived_stats(self):
        """Recalculates all derived stats after a change in base stats."""
        self.max_hp = self._calculate_max_hp()
        self.hp = self.max_hp
        self.max_sp = self._calculate_max_sp()
        self.sp = self.max_sp
        self.attack = self._calculate_attack()
        self.magic_attack = self._calculate_magic_attack()
        self.defense = self._calculate_defense()

    def _calculate_attack(self) -> int:
        return 10 + self.stats["str"]

    def _calculate_magic_attack(self) -> int:
        """Calculates magic attack power based on intelligence."""
        return 5 + self.stats["int"] * 2

    def _calculate_defense(self) -> int:
        return 5 + self.stats["agi"] // 5

    def _calculate_max_hp(self) -> int:
        return 50 + self.stats["vit"] * 10

    def _calculate_max_sp(self) -> int:
        return 10 + self.stats["int"] * 5

    def _calculate_exp_to_next_level(self) -> int:
        return int(100 * (self.level ** 1.5))

    def gain_exp(self, amount: int):
        """Adds experience points and checks for level up."""
        self.exp += amount
        print(f"You gained {amount} experience points.")

        while self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        """Handles the logic for leveling up."""
        self.exp -= self.exp_to_next_level
        self.level += 1
        self.exp_to_next_level = self._calculate_exp_to_next_level()

        print(f"\nCongratulations! You have reached Level {self.level}!")

        # Check for Job Change
        if self.level >= 10 and self.job_class == "Novice":
            self._perform_job_change()

        # Fully restore HP/SP
        self._recalculate_derived_stats() # Recalculate before heal
        self.hp = self.max_hp
        self.sp = self.max_sp

        # Grant stat points
        stat_points_to_distribute = 3
        self.distribute_stat_points(stat_points_to_distribute)

        print(f"\nYour stats after leveling up:")
        self.display_sheet()

    def _perform_job_change(self):
        """Handles the job change process."""
        print("\n--- JOB CHANGE ---")
        print("You have reached Level 10 and can now change your job!")

        available_jobs = list(JOB_CLASSES.keys())

        while True:
            print("\nAvailable jobs:")
            for job_name, job_data in JOB_CLASSES.items():
                print(f"- {job_name}: {job_data['description']}")

            choice = input("Choose your new job: ").capitalize()

            if choice in available_jobs:
                self.job_class = choice
                print(f"\nYou have become a {self.job_class}!")

                # Apply stat bonuses
                bonus = JOB_CLASSES[choice]["stat_bonus"]
                print("You have received a stat bonus!")
                for stat, value in bonus.items():
                    self.stats[stat] += value
                    print(f"  +{value} {stat.upper()}")

                # Grant skills
                for skill_name, skill_data in SKILLS.items():
                    if skill_data["job_class"] == self.job_class:
                        self.skills.append(skill_name)
                        print(f"You have learned the skill: {skill_name}!")

                self._recalculate_derived_stats()
                break
            else:
                print("Invalid choice. Please choose from the list.")

    def distribute_stat_points(self, points: int):
        """Allows the player to distribute a given number of stat points."""
        print(f"\nYou have {points} stat points to distribute.")
        remaining_points = points
        valid_stats = list(self.stats.keys())

        while remaining_points > 0:
            print(f"\nPoints remaining: {remaining_points}")
            self.display_sheet()

            stat_choice = input(f"Enter the stat to increase {valid_stats}: ").lower()
            if stat_choice not in self.stats:
                print("Invalid stat. Please choose from the list.")
                continue

            try:
                point_amount_str = input(f"How many points to add to {stat_choice.upper()}? (1-{remaining_points}) ")
                point_amount = int(point_amount_str)

                if point_amount <= 0 or point_amount > remaining_points:
                    print(f"Invalid amount. Please enter a number between 1 and {remaining_points}.")
                    continue

                self.stats[stat_choice] += point_amount
                remaining_points -= point_amount
                print(f"Added {point_amount} to {stat_choice.upper()}.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        self._recalculate_derived_stats()
        print("\nAll points distributed. Your stats have been updated.")

    def display_sheet(self):
        """Displays the character sheet."""
        print(f"--- Character Sheet ---")
        print(f"Name: {self.name}")
        print(f"Class: {self.job_class}")
        print(f"Level: {self.level} | EXP: {self.exp}/{self.exp_to_next_level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"SP: {self.sp}/{self.max_sp}")
        print(f"ATK: {self.attack} | MATK: {self.magic_attack} | DEF: {self.defense}")
        print(f"--- Stats ---")
        for stat, value in self.stats.items():
            print(f"{stat.upper()}: {value}")
        print(f"-----------------------")
