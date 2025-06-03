define dissenter = Character("The Dissenter")
define recruit = Character("The Recruit")
define leader = Character("The Leader")
define deity = Character("The Deity")

default leader_count = 0
default recruit_count = 0
default good_day_count = 0
default bad_day_count = 0
default good_choice_count = 0
default bad_choice_count = 0

label start:
    scene bg room
    dissenter "This is the intro scene."
    "Here, we will go over the background information of what's going on."
    "Also, we will introduce the main players of the story."
    "It should jump to Day 1 after this..."
    jump day1