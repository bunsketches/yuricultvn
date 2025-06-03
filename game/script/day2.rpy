label day2:
    # Reset good and bad choice counts to 0
    $ good_choice_count = 0
    $ bad_choice_count = 0
    scene bg background3
    marcy "This is the intro of Day 2."
    "This is just some basic setup for the events of the day."
    "Time for the daily prayer to Forever..."
    menu:
        marcy "What should I pray for?"
        "Prayer choice 1":
            "I prayed for choice 1."
        "Prayer choice 2":
            "I prayed for choice 2."
        "Prayer choice 3":
            "I prayed for choice 3."
    marcy "All right, now I need to decide who I will spend time with today: Eleanor, or Sarah."
    menu:
        marcy "Who should I spend time with?"
        "Eleanor":
            marcy "I think I'll spend the day with Eleanor."
            $ eleanor_count += 1
            jump day2_eleanor
        "Sarah":
            marcy "I think I'll spend the day with Sarah."
            $ sarah_count += 1
            jump day2_sarah

label day2_eleanor:
    scene bg background2
    marcy "I am spending the day with Eleanor."
    marcy "This is Dialogue Opportunity 1 for Eleanor, Day 2."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 1 for Eleanor, Day 2."
            $ good_choice_count += 1
        "Bad Choice 1":
            "I chose a Bad Choice for Dialogue Opportunity 1 for Eleanor, Day 2."
            $ bad_choice_count += 1
        "Bad Choice 2":
            "I chose a Bad Choice for Dialogue Opportunity 1 for Eleanor, Day 2."
            $ bad_choice_count += 1
    marcy "This is Dialogue Opportunity 2 for Eleanor, Day 2."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 2 for Eleanor, Day 2."
            $ good_choice_count += 1
        "Bad Choice 1":
            "I chose a Bad Choice for Dialogue Opportunity 2 for Eleanor, Day 2."
            $ bad_choice_count += 1
        "Bad Choice 2":
            "I chose a Bad Choice for Dialogue Opportunity 2 for Eleanor, Day 2."
            $ bad_choice_count += 1
    marcy "This is Dialogue Opportunity 3 for Eleanor, Day 2."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 3 for Eleanor, Day 2."
            $ good_choice_count += 1
        "Bad Choice 1":
            "I chose a Bad Choice for Dialogue Opportunity 3 for Eleanor, Day 2."
            $ bad_choice_count += 1
        "Bad Choice 2":
            "I chose a Bad Choice for Dialogue Opportunity 3 for Eleanor, Day 2."
            $ bad_choice_count += 1
    jump day2_end

label day2_sarah:
    scene bg background2
    marcy "I am spending the day with Sarah."
    marcy "This is Dialogue Opportunity 1 for Sarah, Day 2."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 1 for Sarah, Day 2."
            $ good_choice_count += 1
        "Bad Choice":
            "I chose a Bad Choice for Dialogue Opportunity 1 for Sarah, Day 2."
            $ bad_choice_count += 1
    marcy "This is Dialogue Opportunity 2 for Sarah, Day 2."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 2 for Sarah, Day 2."
            $ good_choice_count += 1
        "Bad Choice":
            "I chose a Bad Choice for Dialogue Opportunity 2 for Sarah, Day 2."
            $ bad_choice_count += 1
    marcy "This is Dialogue Opportunity 3 for Sarah, Day 2."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 3 for Sarah, Day 2."
            $ good_choice_count += 1
        "Bad Choice":
            "I chose a Bad Choice for Dialogue Opportunity 3 for Sarah, Day 2."
            $ bad_choice_count += 1
    jump day2_end

label day2_end:
    scene bg background3
    marcy "This is the end of Day 2. We will compare how many good and bad choices for were made for this day."
    if good_choice_count > bad_choice_count:
        "Looks like we made more good choices than bad. Today was a good day!"
        $ good_day_count += 1
    else:
        "Looks like we made more bad choices than good. Today was a bad day!"
        $ bad_day_count += 1
    marcy "Now we'll jump to Day 3..."
    jump day3
