# Sprite variations
# neutral
# happy
# sad
# upset
# angry
# silly

# Character definitions
define marcy = Character("Marcy")
define sarah = Character("Sarah")
define eleanor = Character("Eleanor")
define forever = Character("Forever")

# Variable declarations
# Count of times player chose to spend time with characters
default eleanor_count = 0
default sarah_count = 0
# Count of good and bad days
default good_day_count = 0
default bad_day_count = 0
# Count of good and bad choices, reset to 0 at the start of each day
default good_choice_count = 0
default bad_choice_count = 0

label start:
    scene bg background1
    marcy "This is the intro scene."
    "Here, we will go over the background information of what's going on."
    "Also, we will introduce the main players of the story."
    "It should jump to Day 1 after this..."
    jump day1