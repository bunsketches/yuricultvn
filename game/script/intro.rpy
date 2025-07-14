# Character definitions
define marcy = Character("Marcy", image="marcy", window_background=Image("gui/textbox_left.png", xalign=0.5, yalign=1.0))
define sarah = Character("Sarah", image="sarah", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))
define eleanor = Character("Eleanor", image="eleanor", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))

# Extra sound channels
init python:
    renpy.music.register_channel("sfx1", "sfx")
    renpy.music.register_channel("sfx2", "sfx")

# Transform definitions
transform left_side:
    zoom 0.75
    anchor (0.5, 1.0)
    pos (0.25, 1.55)

transform right_side:
    zoom 0.75
    anchor (0.5, 1.0)
    pos (0.75, 1.55)

transform center:
    zoom 0.75
    anchor (0.5, 1.0)
    pos (0.5, 1.55)

transform offscreen_left:
    zoom 0.75
    anchor (0.5, 1.0)
    pos (-0.2, 1.55)

transform flip:
    xzoom -1.0

# Variable declarations
# Count of times player chose to spend time with characters
default eleanor_count = 0
default sarah_count = 0
# Count of good and bad days
default eleanor_good_count = 0
default eleanor_bad_count = 0
default sarah_good_count = 0
default sarah_bad_count = 0
# Count of good and bad choices, reset to 0 at the start of each day
default good_choice_count = 0
default bad_choice_count = 0
# Track progression of Forever ending
default secret_end_progress = 0

$ renpy.music.register_channel('loop_sound', 'sfx', loop=True)

label start:
    jump day1
    #menu:
        #"Debug day skip"
        #"Day 1.":
        #    jump day1
        #"Day 2.":
        #    jump day2
        #"Day 3.":
        #    jump day3