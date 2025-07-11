# Character definitions
define marcy = Character("Marcy", image="marcy", window_background=Image("gui/textbox_left.png", xalign=0.5, yalign=1.0))
define sarah = Character("Sarah", image="sarah", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))
define eleanor = Character("Eleanor", image="eleanor", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))
define forever = Character("Forever", image="forever", window_background=Image("gui/textbox_right.png", xalign=0.5, yalign=1.0))

image bg black = Solid('#000000')

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
default good_day_count = 0
default bad_day_count = 0
# Count of good and bad choices, reset to 0 at the start of each day
default good_choice_count = 0
default bad_choice_count = 0
# Track progression of Forever ending
default secret_end_progress = 0

label start:
#    scene bg background3
#    show marcy neutral at left_side
#    marcy "Marcy sprite test"
#    marcy smile "Marcy happy test"
#    show sarah neutral at right_side
#    sarah "Sarah sprite test"
#    sarah happy "Sarah happy test"
#    show eleanor neutral at center
#    eleanor "Eleanor sprite test"
#    eleanor happy "Eleanor happy test"
    menu:
        "Debug day skip"
        "Day 1.":
            jump day1
        "Day 2.":
            jump day2
        "Day 3.":
            jump day3