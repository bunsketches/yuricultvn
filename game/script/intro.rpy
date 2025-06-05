# Character definitions
define marcy = Character("Marcy", image="marcy", window_background=Image("gui/textbox_left.png", xalign=0.5, yalign=1.0))
define sarah = Character("Sarah", image="sarah", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))
define eleanor = Character("Eleanor", image="eleanor", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))
define forever = Character("Forever", image="forever", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))

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
    "This is the intro scene. Here, we will go over the background information of what's going on."
    "Also, we will introduce the main players of the story."
    show marcy neutral at left
    marcy happy "Like me, Marcy, the main character."
    show sarah neutral at right
    sarah happy "And me, Sarah, the new recruit!"
    show eleanor neutral at right
    eleanor happy "And me, Eleanor, the cult leader."
    show forever neutral at right
    forever ". . ."
    "It should jump to Day 1 after this..."
    jump day1