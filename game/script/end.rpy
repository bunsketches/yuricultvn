label end:
    default end_string = ""
    scene bg room
    dissenter "This is the ending scene."
    "First, we will compare how many times we chose The Leader or The Recruit."
    if leader_count > recruit_count:
        "Looks like we spent more time with The Leader."
        $ end_string = "leader"
    else:
        "Looks like we spent more time with The Recruit."
        $ end_string = "recruit"
    "Next, we will compare how many good and bad days we had."
    if good_day_count > bad_day_count:
        "Looks like we had more good days than bad."
        $ end_string += "_good"
    else:
        "Looks like we had more bad days than good."
        $ end_string += "_bad"
    jump expression end_string

label leader_good:
    dissenter "This is the Good Ending with The Leader."
    "It should end the game after this..."
    return

label leader_bad:
    dissenter "This is the Bad Ending with The Leader."
    "It should end the game after this..."
    return

label recruit_good:
    dissenter "This is the Good Ending with The Recruit."
    "It should end the game after this..."
    return

label recruit_bad:
    dissenter "This is the Bad Ending with The Recruit."
    "It should end the game after this..."
    return
