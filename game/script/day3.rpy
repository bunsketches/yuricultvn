label day3:
    $ good_choice_count = 0
    $ bad_choice_count = 0
    scene bg room
    dissenter "This is the intro of Day 3."
    "This is just some basic setup for the events of the day."
    "Time for the daily prayer to The Deity..."
    menu:
        dissenter "What should I pray for?"
        "Prayer choice 1":
            "I prayed for choice 1."
        "Prayer choice 2":
            "I prayed for choice 2."
        "Prayer choice 3":
            "I prayed for choice 3."
    dissenter "All right, now I need to decide who I will spend time with today: The Leader, or The Recruit."
    menu:
        dissenter "Who should I spend time with?"
        "The Leader":
            dissenter "I think I'll spend the day with The Leader."
            $ leader_count += 1
            jump day3_leader
        "The Recruit":
            dissenter "I think I'll spend the day with The Recruit."
            $ recruit_count += 1
            jump day3_recruit

label day3_leader:
    dissenter "I am spending the day with The Leader."
    dissenter "This is Dialogue Opportunity 1 for The Leader, Day 3."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 1 for The Leader, Day 3."
            $ good_choice_count += 1
        "Bad Choice 1":
            "I chose a Bad Choice for Dialogue Opportunity 1 for The Leader, Day 3."
            $ bad_choice_count += 1
        "Bad Choice 2":
            "I chose a Bad Choice for Dialogue Opportunity 1 for The Leader, Day 3."
            $ bad_choice_count += 1
    dissenter "This is Dialogue Opportunity 2 for The Leader, Day 3."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 2 for The Leader, Day 3."
            $ good_choice_count += 1
        "Bad Choice 1":
            "I chose a Bad Choice for Dialogue Opportunity 2 for The Leader, Day 3."
            $ bad_choice_count += 1
        "Bad Choice 2":
            "I chose a Bad Choice for Dialogue Opportunity 2 for The Leader, Day 3."
            $ bad_choice_count += 1
    dissenter "This is Dialogue Opportunity 3 for The Leader, Day 3."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 3 for The Leader, Day 3."
            $ good_choice_count += 1
        "Bad Choice 1":
            "I chose a Bad Choice for Dialogue Opportunity 3 for The Leader, Day 3."
            $ bad_choice_count += 1
        "Bad Choice 2":
            "I chose a Bad Choice for Dialogue Opportunity 3 for The Leader, Day 3."
            $ bad_choice_count += 1
    jump day3_end

label day3_recruit:
    dissenter "I am spending the day with The Recruit."
    dissenter "This is Dialogue Opportunity 1 for The Recruit, Day 3."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 1 for The Recruit, Day 3."
            $ good_choice_count += 1
        "Bad Choice":
            "I chose a Bad Choice for Dialogue Opportunity 1 for The Recruit, Day 3."
            $ bad_choice_count += 1
    dissenter "This is Dialogue Opportunity 2 for The Recruit, Day 3."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 2 for The Recruit, Day 3."
            $ good_choice_count += 1
        "Bad Choice":
            "I chose a Bad Choice for Dialogue Opportunity 2 for The Recruit, Day 3."
            $ bad_choice_count += 1
    dissenter "This is Dialogue Opportunity 3 for The Recruit, Day 3."
    menu:
        "What should I do?"
        "Good Choice":
            "I chose a Good Choice for Dialogue Opportunity 3 for The Recruit, Day 3."
            $ good_choice_count += 1
        "Bad Choice":
            "I chose a Bad Choice for Dialogue Opportunity 3 for The Recruit, Day 3."
            $ bad_choice_count += 1
    jump day3_end

label day3_end:
    dissenter "This is the end of Day 3. We will compare how many good and bad choices for were made for this day."
    if good_choice_count > bad_choice_count:
        "Looks like we made more good choices than bad. Today was a good day!"
        $ good_day_count += 1
    else:
        "Looks like we made more bad choices than good. Today was a bad day!"
        $ bad_day_count += 1
    dissenter "Now we'll jump to the ending..."
    jump end
