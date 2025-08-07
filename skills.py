# skills.py
# This file defines the skills available in the game.

SKILLS = {
    "Bash": {
        "name": "Bash",
        "description": "A powerful single-target strike.",
        "sp_cost": 8,
        "damage_type": "Physical",
        "damage_multiplier": 1.5, # 150% of physical attack
        "job_class": "Swordsman"
    },
    "Fire Bolt": {
        "name": "Fire Bolt",
        "description": "Hurls a bolt of fire at an enemy.",
        "sp_cost": 12,
        "damage_type": "Magic",
        "damage_multiplier": 1.7, # 170% of magic attack
        "job_class": "Mage"
    },
    "Double Strafe": {
        "name": "Double Strafe",
        "description": "Fires two arrows at once.",
        "sp_cost": 10,
        "damage_type": "Physical",
        "damage_multiplier": 1.4, # Represents the combined power
        "job_class": "Archer"
    }
}
