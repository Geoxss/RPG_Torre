# main.py
# This file will contain the main game loop.

from character import Player

def main():
    """
    The main function for the game.
    """
    print("Welcome to the Infinite Tower RPG!")
    print("Let's create your character.")

    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    print("\nCharacter created successfully!")
    player.display_sheet()

    print("\nYou are now ready to enter the tower.")
    # Placeholder for the tower loop
    while True:
        print("\n--- Floor 1 ---")
        print("A wild monster appears!")
        # Placeholder for combat
        print("You defeated the monster!")
        print("You ascend to the next floor.")
        break # Just run once for now

if __name__ == "__main__":
    main()
