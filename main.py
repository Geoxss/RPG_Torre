# main.py
# This file will contain the main game loop.

import time
from character import Player
from monster import Monster

def combat(player: Player, monster: Monster):
    """
    Handles the combat between a player and a monster.
    """
    print(f"\nA wild {monster.name} appears!")
    monster.display_info()
    time.sleep(1)

    # Simple turn-based combat
    while player.hp > 0 and monster.is_alive():
        # Player's turn
        print(f"\n{player.name}'s turn. HP: {player.hp}/{player.max_hp} | SP: {player.sp}/{player.max_sp}")

        action_taken = False
        while not action_taken:
            print("Choose your action:")
            print("  1. Attack")
            print("  2. Skills (Not Implemented)")
            print("  3. Items (Not Implemented)")

            choice = input("> ")

            if choice == "1":
                player_damage = max(0, player.attack - monster.defense)
                monster.hp -= player_damage
                print(f"You attack the {monster.name} for {player_damage} damage.")
                print(f"{monster.name}'s HP: {monster.hp}/{monster.max_hp}")
                action_taken = True
            elif choice == "2":
                print("Skill system not implemented yet. You lose a turn.")
                action_taken = True
            elif choice == "3":
                print("Item system not implemented yet. You lose a turn.")
                action_taken = True
            else:
                print("Invalid choice. Please enter a valid number.")

        time.sleep(1)

        if not monster.is_alive():
            print(f"\nYou defeated the {monster.name}!")
            # player.gain_exp(monster.xp_reward) # To be implemented
            return

        # Monster's turn
        print(f"\n{monster.name}'s turn.")
        monster_damage = max(0, monster.attack - player.defense)
        player.hp -= monster_damage
        print(f"The {monster.name} attacks you for {monster_damage} damage.")
        print(f"{player.name}'s HP: {player.hp}/{player.max_hp}")
        time.sleep(1)

    if player.hp <= 0:
        print("\nYou have been defeated. Game Over.")
        # End game or respawn logic here

def main():
    """
    The main function for the game.
    """
    print("Welcome to the Infinite Tower RPG!")
    print("Let's create your character.")

    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    print("\nCharacter created!")
    player.distribute_stat_points(10) # Give 10 points to distribute

    print("\nYour final character sheet:")
    player.display_sheet()

    print("\nYou are now ready to enter the tower.")

    # --- Tower Loop ---
    floor = 1
    while player.hp > 0:
        print(f"\n--- Floor {floor} ---")

        # Spawn a monster for the floor
        # For now, it's always a Poring
        current_monster = Monster(name="Poring", hp=30, attack=8, defense=2, xp_reward=50)

        # Store player hp before combat to check for victory
        hp_before_combat = player.hp
        combat(player, current_monster)

        # Check if player won the combat
        if player.hp > 0 and hp_before_combat > 0: # Second condition for clarity
            print(f"\nYou defeated the {current_monster.name}!")
            player.gain_exp(current_monster.xp_reward)

            print("\nYou feel refreshed and ascend to the next floor.")
            # Restore HP/SP after battle for now
            player.hp = player.max_hp
            player.sp = player.max_sp
            floor += 1
            time.sleep(2)
        else:
            break

if __name__ == "__main__":
    main()
