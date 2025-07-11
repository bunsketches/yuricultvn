label day1:
    # Reset good and bad choice counts to 0
    $ good_choice_count = 0
    $ bad_choice_count = 0
    scene bg sunrise with fade
    "A lighter clicks, a flame blossoms."
    "There is a circle, drawn into the dirt, with a small stone statue of a mysterious woman in the center."
    "She is dimmed by candlelight. Wisps of incense smoke waft behind her from a myrrh stick."
    "An obsidian scrying mirror reflects your face from the shadows as you approach the circle."
    show marcy neutral at left_side with dissolve
    marcy neutral "Morning prayer..."
    menu:
        marcy neutral "What should I pray for?"
        "Offer your praise to the altar":
            "You place cut flowers onto the altar, reciting the usual litany."
            marcy neutral "I love Forever, as Forever loves me."
        "Pray for yourself":
            marcy neutral "I've known your embrace for almost my entire life. Yet even now... I feel nothing."
            marcy neutral "I don't know if I know how to... never mind. Good morning."
            $ secret_end_progress += 1
        "Do not pray":
            marcy neutral "Forget about it."
    "You look up, the glare blinding you for a moment. Above is the open blue sky and sunshine, bright and warm. Birdsong hangs in the air."
    "It takes a moment of settling in with the beauty of the painfully vibrant day before you start on your chores."
    show bg outside with dissolve
    "Here at Aeuternum, everyone must do their part. Today, your part is to fetch water."
    show sarah worried at right_side with dissolve
    "On your way to the river, you bump into a tall, soft girl with preppy hair. Her strong arms release something large - a clay vase."
    "There is a loud splash as water spills from the vase, dousing the girl and pooling on the ground."
    show eleanor neutral at center, flip with dissolve
    "A blonde woman arrives soon after, her expression calm and inscrutable."
    eleanor neutral "Ah - good morning, Marcy. It appears I've come at a bad time..."
    eleanor happy "This is Sarah, our newest member and an absolutely lovely addition to our family."
    show sarah neutral
    eleanor neutral "That being said, could I steal you for a moment?"
    show sarah worried
    "You look at Sarah, who is exasperatedly fumbling with vases."
    menu:
        marcy "Who should I go with?"
        "Go help Sarah":
            marcy "Eleanor, I knocked over all this water Sarah was carrying. I should help her refill it. Can we talk another time?"
            "Eleanor beams that soft, serene smile of hers, one you've seen many times."
            hide eleanor with dissolve
            "With a nod, she turns to leave respectfully. In turn, you and Sarah head for the river."
            $ sarah_count += 1
            jump day1_sarah
        "Follow Eleanor":
            marcy concern "Of course, Eleanor. Lead the way."
            show sarah neutral
            "Off to the side, Sarah gathers herself, picking up the vase and carrying it back to the river."
            hide sarah with dissolve
            show marcy neutral
            "Eleanor smiles, calm and collected as always."
            eleanor happy "Good. This way."
            $ eleanor_count += 1
            jump day1_eleanor

label day1_sarah:
    scene bg river with dissolve
    "Once you reach the river with Sarah, she dips the vase into the cool waters beside you."
    show marcy neutral at left_side with dissolve
    show sarah happy at right_side with dissolve
    sarah happy "It's so silly how that happened. I can't believe I walked right into you! Thanks for coming with me, I appreciate your help."
    marcy neutral "..."
    sarah neutral "..."
    sarah happy "Oh! I never got your name. What do I call you?"
    marcy neutral "The name's Marcy."
    sarah happy "Nice to meet you, Marcy."
    marcy neutral "Uh huh."
    scene bg day1 sarah with dissolve
    "Sarah continues filling water and trades the vase off with you for you to fill it."
    menu:
        sarah neutral "So, how did you join Aeuternum?"
        "I left my life behind when Eleanor met me. She took me in.":
            sarah happy "Me too! I went to school with Eleanor and..."
            sarah worried "I had to run from home."
            sarah happy "Eleanor made an offer when that happened, so here I am."
            "Sarah pauses for a moment while she reminisces, smiling fondly at the running river water below her.\nYou then watch her shake her head, seemingly snapping out of whatever daydream she was in, facing you again."
            $ good_choice_count += 1
        "It's private.":
            show sarah worried
            "Sarah jumps a bit, surprised at the blunt remark. You see her fumble with her vase, almost dropping it before laughing nervously."
            sarah worried "Oh - I'm sorry, I didn't mean to make you uncomfortable."
            sarah worried "It's just that, I swear that everyone here's got a similar story to tell..."
            $ bad_choice_count += 1
    menu:
        sarah neutral "So... Are you a day or a night person?"
        "Day.":
            sarah neutral "Huh. Well, suit yourself! But, the day is truly glorious in its own way."
            "Sarah continues filling a vase with water. The air around you two thickens, and not just because of the oncoming summer heat. Silence fills the air, but Sarah doesn't seem to mind, humming a random tune all the while. You turn to look at the sky just as she clears her throat, prompting you with another question."
            $ bad_choice_count += 1
        "Night.":
            sarah happy "Hey, that makes two of us! I just love the sky when it clears, and seeing all of the stars shine."
            sarah happy "That is something that I do like here... We're far away from all the light pollution."
            "You cock your head at Sarah. Clouds move and clear away to beam light directly onto where the pair of you are, warming your skin."
            marcy neutral "Light pollution?"
            sarah happy "You've never heard it? Hmm, it's like when lights from buildings and stuff are too bright to see the stars at night."
            "You shake your head. You've lived here for almost as long as you can remember. The terminology doesn't ring a bell."
            marcy neutral "I guess we don't have that problem here, no."
            $ good_choice_count += 1
    menu:
        sarah neutral "How is it, getting used to Aeuternum? Any tips you can give a new friend?"
        "Friend? I just met you.":
            sarah worried "Oh, right - I guess I am getting ahead of myself."
            sarah neutral "Well, you're my friend now!"
            "You tilt your head at her, half-scowl on your face, but she doesn't miss a beat."
            $ bad_choice_count += 1
        "Yeah - do your prayers and always contribute. That's kept me out of trouble.":
            sarah happy "Thanks! I'll keep that in mind. I'm so nervous! I want to do my best to fit in and feel at home."
            "She flashes a toothy grin at you, genuinely happy. You'd think she won the lottery, not doing manual labor."
            $ good_choice_count += 1
    scene bg river with dissolve
    show marcy neutral at left_side with dissolve
    show sarah neutral at right_side with dissolve
    "Sarah hums as she takes the vase back and brings herself to her feet with the vase of water."
    sarah happy "It was great talking to you, Marcy! I'm going to go ahead and bring this back to the dining hall. I'll see you later!"
    hide sarah with dissolve
    "Sarah walks off with the heavy vase, giving you one last bright smile before leaving you at the river."
    marcy neutral "Interesting girl..."
    "You look at your feet, and listen to the sounds of the forest and river around you."
    marcy neutral "I guess a fresh face wouldn't hurt."
    "Deciding you've spent enough time dilly-dallying, you trudge in the direction back to  Aeuternum. More chores are to be done for the day."
    jump day1_end

label day1_eleanor:
    scene bg garden1 with dissolve
    show marcy neutral at left_side with dissolve
    show eleanor neutral at right_side with dissolve
    "You join Eleanor in the garden. She picks a daisy from one of the flowerbeds, regarding it calmly while twirling it in her fingers."
    eleanor playful "Daisies... the flower of innocence, purity... does it remind you of anyone?"
    show marcy uneasy
    show eleanor delighted
    "You're caught a bit off guard, unsure of what to say. You've been at Aeuternum for years, and yet you're still not used to the way Eleanor speaks."
    "Everything that comes out of her mouth is spoken so sweetly, but still feels like some sort of trap."
    "You keep your distress mostly clear off your face as always, in spite of the heat crawling up your neck. Eleanor, keen-eyed as always, laughs before you can recover."
    "Softly, she asks you a question."
    eleanor neutral "Do you know why I brought you here, Marcy?"
    marcy neutral "I do not."
    "Eleanor looks out into the openness of the freshly watered garden, shimmering with vibrance. The smell of wet soil and dewy grass hangs in the air."
    scene bg day1 eleanor1 with dissolve
    eleanor happy "To check in on you, my friend."
    "Eleanor turns her gaze to you."
    show bg day1 eleanor2 with dissolve
    menu:
        eleanor happy "The garden is beautiful, is it not?"
        "It has been growing so well, I agree.":
            "Eleanor nods in agreement, seemingly delighted at your approval."
            "The thought of Eleanor, of all people, seeking the approval of anyone, seems ridiculous."
            "But you keep that to yourself."
            eleanor happy "You've done great work here, Marcy."
            $ good_choice_count += 1
        "We could do better.":
            "Eleanor glances at you, surprised, then turns back."
            eleanor neutral "There is always room for improvement, Marcy - even when it all seems perfect."
            "You hum in acknowledgement, but out of your peripheral vision, you catch her staring, her gaze fixed on your profile."
            "From anyone else, it would have been an agreement. From Eleanor though, it feels like scolding. Despite the harsh sunlight, you feel your body run a bit cold."
            $ bad_choice_count += 1
        "It looks awful.":
            "Eleanor smiles, cold and mirthless. Despite it being almost summer, you feel a chill descend around the two of you, and shiver."
            eleanor neutral "Nonsense."
            "From anyone else, it would have been a gentle reassurance. From Eleanor though, it feels like scolding."
            $ bad_choice_count += 1
    menu:
        eleanor happy "And how has Aeuternum been treating you all these years, dear?"
        "I... am still figuring it out.":
            "Eleanor presses the daisy to their nose, the edges of her lips curling into a smile."
            eleanor happy "Excellent, Marcy. Excellent. You owe no debts to me - it has been a pleasure having you with us."
            "You're not sure what to say in response, so you don't say anything. Your body has faced toward the flowerbeds this whole conversation, but Eleanor's eyes still meet yours from the side."
            "She can tell you're waiting for her to say something more."
            $ bad_choice_count += 1
        "I have been finding myself here because of you. I am indebted.":
            "You reach your hand to scratch at your scar subconsciously. Before you can complete the compulsive action, Eleanor hands you a daisy."
            eleanor happy "Take all of the time you need. Trust in Forever's guidance, and you'll find yourself when the time is right."
            $ good_choice_count += 1
        "It's nice, I guess.":
            "Eleanor laughs a little. It's light, and you can tell she finds real humor in an otherwise awkward and tense situation. Is she enjoying seeing you squirm?"
            eleanor neutral "It's unhealthy to be so unsure of yourself, Marcy. Relax a little. This is your home."
            "You feel like she's toying with you somehow. You squint up at the sun, trying to avoid her gaze, but find your eyes gravitating toward her anyway."
            $ bad_choice_count += 1
    menu:
        eleanor happy "Marcy... Keep up the good work. I am watching you."
        "Of course. I'll continue to work hard, Eleanor.":
            "Eleanor chuckles at you, nodding approvingly. She moves to leave, but not without reaching up to pat the top of your head."
            "She's quite a bit shorter than you, so as if moving on autopilot, you duck your head so that she can reach. You watch her saunter off, grace in every step." 
            "Stunned at the sudden act of what can only be confusingly described as affection, you now stand alone in the garden, sun beaming down, daisies not quite in full bloom."
            $ good_choice_count += 1
        "Please don't.":
            "If your rebuke has any effect on Eleanor, it doesn't show. Eleanor gestures for you to leave."
            "Her usual smile is not angry, but it's certainly not satisfied."
            $ bad_choice_count += 1
        "...":
            "Matching your silence, Eleanor gestures for you to leave."
            "Her usual smile is not angry, but it's certainly not satisfied."
            $ bad_choice_count += 1
    jump day1_end

label day1_end:
    scene bg house1 with dissolve
    show marcy neutral at left_side with dissolve
    marcy neutral "Well, that sure was... something."
    menu:
        marcy neutral "Wonder what I should do for the rest of the day?"
        "Mop the floors.":
            show bg hallway with dissolve
            "You spend the rest of the evening grabbing a bucket and a mop, trailing suds as you work across the floor. After an hour, the floors are spotless, with a near-mirror shine."
        "Work on food prep":
            show bg kitchen with dissolve
            "You walk into the kitchen, tying an apron around your waist. You spend the hour chopping, slicing, and peeling like nobody's business. The repetitive, mechanical motions are strangely relaxing, putting you in an almost meditative state."
        "Dust the basement.":
            show bg basement with dissolve
            "You spend the rest of your time in the dark of the basement, a lantern lighting your way as you clear away the dust and cobwebs. When you finish, the air feels a lot less musty, a very welcome burst of freshness."
    show bg dining with dissolve
    "You wrap up your chores and join everyone in the dining hall for dinner."
    "At the end of the meal, everyone receives a chalice of wine, a sacrament of sorts."
    "The wine is heavy on your tongue, an oddly savory taste that took some getting used to when you first came here."
    "But now you welcome the hint of spice and that warming feeling, as the aches and pains of the day's work melt away."
    "As you unwind, you hear murmurs behind you..."
    "Gossipping Devotee" "She seems jealous."
    "Fellow Devotee" "Of what? That's unusual."
    marcy uneasy "..."
    "You never cared for those who talk as if no one can hear them. You finish your drink, and rise silently. Your feet drag back to your quarters for the night, the chatter fading with distance."
    show bg bedroom with dissolve
    "With the day coming to an end, you climb into bed, soft bedding at odds with the rough matress. The bedding wins, most nights."
    "The springs creak under your weight, and your eyes grow heavy once their face hits the cool side of the pillow. You drift into a dull, numbing slumber."
    show bg black with dissolve

    if good_choice_count > bad_choice_count:
        $ good_day_count += 1
    else:
        $ bad_day_count += 1
    jump day2
