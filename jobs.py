# jobs.py
# This file defines the job classes available in the game.

JOB_CLASSES = {
    "Swordsman": {
        "description": "A master of the sword, focusing on strength and physical combat.",
        "stat_bonus": {
            "str": 5,
            "vit": 3,
            "agi": 2,
        }
        # In the future, we can add things like:
        # "base_skills": ["Bash", "Magnum Break"]
    },
    "Mage": {
        "description": "A powerful spellcaster who commands the elements.",
        "stat_bonus": {
            "int": 5,
            "dex": 3,
            "vit": 2,
        }
        # "base_skills": ["Fire Bolt", "Cold Bolt"]
    },
    "Archer": {
        "description": "A nimble marksman who excels at long-range attacks.",
        "stat_bonus": {
            "dex": 5,
            "agi": 3,
            "luk": 2,
        }
        # "base_skills": ["Double Strafe", "Arrow Shower"]
    }
}
