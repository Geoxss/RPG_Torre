# main.py
# This file will contain the main game loop.

import time
from character import Player
from monster import Monster
from skills import SKILLS

def combat(player: Player, monster: Monster):
    """
    Handles the combat between a player and a monster.
    Returns True if the player wins, False otherwise.
    """
    print(f"\nA wild {monster.name} appears!")
    monster.display_info()
    time.sleep(1)

    while player.hp > 0 and monster.is_alive():
        # Player's turn
        print(f"\n{player.name}'s turn. HP: {player.hp}/{player.max_hp} | SP: {player.sp}/{player.max_sp}")

        action_taken = False
        while not action_taken:
            print("Choose your action:")
            print("  1. Attack")
            print("  2. Skills")
            print("  3. Items (Not Implemented)")

            choice = input("> ")

            if choice == "1": # Basic Attack
                player_damage = max(0, player.attack - monster.defense)
                monster.hp -= player_damage
                print(f"You attack the {monster.name} for {player_damage} damage.")
                print(f"{monster.name}'s HP: {monster.hp}/{monster.max_hp}")
                action_taken = True
            elif choice == "2": # Skills
                if not player.skills:
                    print("You have not learned any skills yet.")
                    continue # Let player choose another action

                print("Choose a skill:")
                for i, skill_name in enumerate(player.skills, 1):
                    skill_data = SKILLS[skill_name]
                    print(f"  {i}. {skill_name} (SP: {skill_data['sp_cost']}) - {skill_data['description']}")
                print(f"  {len(player.skills) + 1}. Cancel")

                skill_choice_str = input("> ")
                try:
                    skill_choice = int(skill_choice_str)
                    if skill_choice == len(player.skills) + 1:
                        continue # Go back to action menu

                    selected_skill_name = player.skills[skill_choice - 1]
                    skill = SKILLS[selected_skill_name]

                    if player.sp >= skill['sp_cost']:
                        player.sp -= skill['sp_cost']

                        if skill['damage_type'] == 'Physical':
                            base_damage = player.attack
                        else: # Magic
                            base_damage = player.magic_attack

                        skill_damage = int(base_damage * skill['damage_multiplier'])
                        final_damage = max(0, skill_damage - monster.defense)

                        monster.hp -= final_damage
                        print(f"You use {skill['name']} on {monster.name} for {final_damage} damage!")
                        print(f"{monster.name}'s HP: {monster.hp}/{monster.max_hp}")
                        action_taken = True
                    else:
                        print("Not enough SP to use this skill.")
                except (ValueError, IndexError):
                    print("Invalid skill choice.")

            elif choice == "3": # Items
                print("Item system not implemented yet. You lose a turn.")
                action_taken = True
            else:
                print("Invalid choice. Please enter a valid number.")

        time.sleep(1)

        if not monster.is_alive():
            break # Player wins

        # Monster's turn
        print(f"\n{monster.name}'s turn.")
        monster_damage = max(0, monster.attack - player.defense)
        player.hp -= monster_damage
        print(f"The {monster.name} attacks you for {monster_damage} damage.")
        print(f"{player.name}'s HP: {player.hp}/{player.max_hp}")
        time.sleep(1)

    if player.hp <= 0:
        print("\nYou have been defeated. Game Over.")
        return False
    else:
        return True

def main():
    """
    The main function for the game.
    """
    print("Welcome to the Infinite Tower RPG!")
    print("Let's create your character.")

    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    print("\nCharacter created!")
    player.distribute_stat_points(10)

    print("\nYour final character sheet:")
    player.display_sheet()

    print("\nYou are now ready to enter the tower.")

    # --- Tower Loop ---
    floor = 1
    while player.hp > 0:
        print(f"\n--- Floor {floor} ---")

        # Determine which monster to spawn based on the floor
        monster_to_spawn = "Poring" # Default
        if floor >= 4 and floor < 7:
            monster_to_spawn = "Fabre"
        elif floor >= 7 and floor < 10:
            monster_to_spawn = "Lunatic"
        elif floor >= 10:
            monster_to_spawn = "Hornet"

        current_monster = Monster(name=monster_to_spawn)

        player_won = combat(player, current_monster)

        if player_won:
            print(f"\nYou defeated the {current_monster.name}!")
            player.gain_exp(current_monster.xp_reward)

            print("\nYou feel refreshed and ascend to the next floor.")
            player.hp = player.max_hp
            player.sp = player.max_sp
            floor += 1
            time.sleep(2)
        else:
            # Player was defeated, game over message is in combat()
            break

if __name__ == "__main__":
    main()
