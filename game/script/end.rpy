label end:
    default end_string = ""
    scene bg background3
    marcy "This is the ending scene."
    "First, we will compare how many times we chose Eleanor or Sarah."
    if eleanor_count > sarah_count:
        "Looks like we spent more time with Eleanor."
        $ end_string = "eleanor"
    else:
        "Looks like we spent more time with Sarah."
        $ end_string = "sarah"
    "Next, we will compare how many good and bad days we had."
    if good_day_count > bad_day_count:
        "Looks like we had more good days than bad."
        $ end_string += "_good"
    else:
        "Looks like we had more bad days than good."
        $ end_string += "_bad"
    jump expression end_string

label eleanor_good:
    scene bg background1
    marcy "This is the Good Ending with Eleanor."
    "It should end the game after this..."
    return

label eleanor_bad:
    scene bg background1
    marcy "This is the Bad Ending with Eleanor."
    "It should end the game after this..."
    return

label sarah_good:
    scene bg background1
    marcy "This is the Good Ending with Sarah."
    "It should end the game after this..."
    return

label sarah_bad:
    scene bg background1
    marcy "This is the Bad Ending with Sarah."
    "It should end the game after this..."
    return
