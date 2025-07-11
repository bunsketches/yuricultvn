label day2:
    # Reset good and bad choice counts to 0
    $ good_choice_count = 0
    $ bad_choice_count = 0
    scene bg sunrise with fade
    play sound "sfx/rooster.mp3"
    play music "sfx/forest.mp3" fadein 1.0
    "You wake fully rested. You hesitate climbing out of the sheets into the cold morning. The bite of the air rushes into your lungs, clearing your mind, as you begin the day."
    "Your morning routine is a blur, and you soon find yourself before Forever's altar, ready for morning prayer."
    $ renpy.music.set_volume(0.25, 0.0)
    if secret_end_progress >= 1:
        "It might be a trick of the light, but Forever's idol seems... larger than before, if not in physical size, then in presence at least."
    "Your face appears in the scrying mirror by the candlelight, as you gather your thoughts."
    show marcy neutral at left_side with dissolve
    menu:
        marcy neutral "What should I pray for?"
        "Offer your praise to the altar":
            "You went and picked up a piece of bread from the dining hall in the morning to offer to the altar, next to the other offerings the others had laid out before."
            marcy neutral "Good morning. Just my way of saying, 'Thanks'. Hope you like it. I'll see you again tomorrow."
        "Pray for yourself":
            "You clasp your hands together, shutting your eyes tight. It feels like something in you is slipping away, and you are desperately trying to get it back."
            marcy neutral "Are you real? I've prayed to you every morning, and I still feel the same..."
            marcy neutral "Please help me get through this, even if it's just for today."
            $ secret_end_progress += 1
        "Do not pray":
            "You shake your head with a sigh. It feels like something inside you has shifted as of late. Your arms hang lamely at your sides."
            "While this statue may have filled you with a refreshing sense of hope just a year or two ago, lately you find yourself looking up at it with tired eyes, its presence looming above you."
            marcy neutral "Why am I here?"
    show bg outside with dissolve
    "You exit the shed, and are greeted by a glorious new day. The wind whistles quietly through the tree branches."
    marcy neutral "All right, time to get to it, I guess."
    menu:
        marcy "What should I take care of today?"
        "Tend Garden":
            scene bg garden2 with fade
            "As you go about your task, you run into Sarah."
            $ sarah_count += 1
            jump day2_sarah
        "Collect River Water":
            scene bg river with fade
            "As you go about your task, you run into Eleanor."
            $ eleanor_count += 1
            jump day2_eleanor
        "Prepare the Dining Room":
            scene bg dining with fade
            "As you go about your task, you run into Eleanor."
            $ eleanor_count += 1
            jump day2_eleanor
        "Organize the Kitchen":
            scene bg kitchen with fade
            "As you go about your task, you run into Eleanor."
            $ eleanor_count += 1
            jump day2_eleanor
        "Mop the Hallway":
            scene bg hallway with fade
            "As you go about your task, you run into Sarah."
            $ sarah_count += 1
            jump day2_sarah
        "Tidy the Basement":
            scene bg basement with fade
            "As you go about your task, you run into Sarah."
            $ sarah_count += 1
            jump day2_sarah

label day2_eleanor:
    show eleanor neutral at right_side with dissolve
    eleanor happy "Marcy! Come join me in the kitchen. We need your help."
    "As she speaks to you, you see the glimmer of some unknown intent in her calculating gaze, partially masked by her inviting smile."
    scene bg kitchen with fade
    show marcy neutral at left_side with dissolve
    show eleanor neutral at right_side with dissolve
    "Eleanor tasks you with cutting meat and ingredient prep in the kitchen. For reasons known only to her, she follows you there."
    "Eleanor fills the silence with remarks about you, comparing you to herself when she got started at Aeuternum."
    "The otherwise innocent small talk is barbed with occasional questions about Sarah, laced with a bitter edge of jealousy."
    "Eleanor lays a leg of ham on the butcher block and gestures at it."
    eleanor "Be a dear and portion out the ham, would you, Marcy?"
    scene bg day2 eleanor1 with fade
    "As you get to hacking the large cut of meat into more manageable pieces, Eleanor stands beside you, patiently stirring a large pot of broth."
    eleanor "You know, I started off without a goal. Did you know that?"
    "You listen while chopping the meat into rough, ragged chunks. Eleanor smiles."
    eleanor "There was just something about my life back then that was... lacking."
    "Eleanor glances at you, still stirring the pot."
    menu:
        eleanor "What is your purpose here, Marcy?"
        "To be loved, and to learn to love. To be Forever's Chosen, of course.":
            eleanor "Good girl. I've seen you pray to Her every morning, and I am sure the goddess has noticed your efforts."
            eleanor "It is our duty as her lovers to show our loyalty."
            $ good_choice_count += 1
        "To figure out my life. I am still getting there.":
            eleanor "Your life begins here. I wouldn't miss the opportunity if I were you, Marcy."
            "You don’t miss the warning tone in Eleanor’s bluntness, though someone like Sarah probably would."
            "This is just how Eleanor navigates conversation. Her pleasantries aren’t so much a mask as they are a part of her. Her demeanor doesn’t break, it bends."
            $ bad_choice_count += 1
        "I don't know.":
            "Eleanor clicks her tongue softly."
            eleanor "To take your shots aimlessly is to miss the chances that were right before you, Marcy. Don't be selfish - missing those chances here is careless."
            "Eleanor says the words sweetly, as if she were gently chiding a puppy. Still, you feel the sting. The word “selfish” echoes in your head as you’re left to ponder such an assessment of your character."
            "Still, you can’t find it in you to argue, much less against someone like Eleanor. She’d find a way to make her statement true regardless."
            $ bad_choice_count += 1
    "Eleanor looks down at her reflection in the simmering broth. As she stirs over the flame, you notice that she’s barely tall enough to comfortably stir such a large stockpot. You almost chuckle a bit at the mental image of Eleanor needing a step stool to reach the burners."
    "Before you can entertain the thought further, Eleanor begins speaking again. Her tone, lovely as always, but still cautious and calculated:"
    menu:
        eleanor happy "And how is Sarah fitting in?"
        "Sarah does her best, from what I can tell.":
            eleanor neutral "I'll watch her."
            "You don’t doubt that Eleanor means that. She keeps tabs on everyone at Aeuternum, and always seems to know more about people than they do themselves."
            "Some find it comforting, others find it disconcerting. The latter usually don’t stay here too long. You have no opinion of it. That’s just… Eleanor."
            $ bad_choice_count += 1
        "Sarah is a bit clumsy. How did you two meet?":
            "Eleanor chuckles at your assessment and question."
            eleanor happy "She is a mess for the goddess, but I know she'll grow into a strong lover for Forever."
            "Eleanor puffs air through her nose, a half laugh as she recalls the memory."
            eleanor neutral "Poor thing... I found her unconscious and bruised outside of the school I used to go to."
            eleanor neutral "The hour was dark. She had no one. The world certainly did not love her as well as she deserved."
            "It surprises you how almost genuine Eleanor seems in her recollection."
            "You’ve known Eleanor for a long time, but less as a friend and more as a mentor. She’s led since you were both younger. Though she used to seem a little less eerily perfect, she’s always been a bit enigmatic."
            "Even back then she never really talked about her personal life. School, friends, family, anything like that, are all things still shrouded in mystery around Eleanor."
            $ bad_choice_count += 1
        "Sarah does not belong here.":
            "Eleanor raises her brows in surprise."
            eleanor neutral "Is that so? Tough words against someone who is new, Marcy... but I'll keep an eye on her, if you're so sure."
            "You almost laugh at the irony of Eleanor scolding you for being harsh."
            "Well, you suppose she’s right in a way: you’ve always been a bit more curt than others."
            "You believe what you said though, and part of you thinks that Eleanor agrees. Where Eleanor can see past pretty much anyone, sometimes you think you’re one of the only ones who can catch even a glimpse of her."
            $ good_choice_count += 1
    "Eleanor taps the spoon against the pot, leaving the broth to simmer. She sets the stirring spoon aside on a cloth and appraises your work."
    "The action startles you out of your thoughts and you tense up a bit. Noticing this, Eleanor attempts to shrug your shoulders back down, smoothing her hands down from your collar."
    show bg day2 eleanor2 with dissolve
    eleanor happy "I have enjoyed seeing how you've grown with us, Marcy. I enjoy this time I share with you, seeing how far you've come since the day I brought you here."
    "Eleanor places a clean hand on your arm, the touch electric even after all this time."
    eleanor happy "And now that we are sharing this moment, I have a proposal for you."
    marcy neutral "A proposal?"
    menu:
        eleanor happy "Be my Second, my right hand in all things. For Forever, for our lovers. I want you to guide them by my side, and feel closer to Her. Together."
        "Eleanor... This feels so sudden. I don't know if I am ready. I'm sorry.":
            eleanor neutral "Of course you are ready, Marcy. But I understand that this is sudden for you. You can take your time to think about it, if you'd like."
            "Eleanor responds calmly, as if her desired outcome is inevitable. She was born into affluence, after all. You wonder briefly if anyone’s ever told her “No” before responding."
            marcy neural "Sure."
            "Apparently, you won’t today, either."
            $ bad_choice_count += 1
        "I can't. You should look for someone more qualified.":
            "Eleanor’s response is already on the tip of her tongue before you can finish your sentence. Still, politely, she waits just until you finish."
            eleanor neutral "Your aim is lacking, Marcy."
            "True to her word, you look down and notice a small cut on your knuckle where you’ve cut yourself having cut the ham absentmindedly."
            "You wince a bit, bringing your hand to your mouth to suck on the wound briefly. Eleanor seems to watch the action with great interest."
            $ bad_choice_count += 1
        "Really? Beside you? This is an honor...":
            marcy smile "I don't know what to say. Can I at least think about it tonight?"
            "Eleanor's smile is the brightest you've seen it.\nIt almost reaches her eyes, even.\nAlmost."
            "Even now, there is a gleam of mysterious intent in her gaze."
            eleanor happy "Of course, my dear. Think about it, and come find me tomorrow."
            $ good_choice_count += 1
    show bg kitchen with dissolve
    show marcy neutral at left_side with dissolve
    show eleanor neutral at right_side with dissolve
    "Eleanor pats you on the back."
    eleanor happy "Cook and serve in the dining hall this afternoon. I will be seeing you, Marcy."
    "Eleanor leaves without another word."
    hide eleanor with dissolve
    "As the others find their way to the dining hall for lunchtime, you see Sarah in the crowd."
    show sarah worried at right_side with dissolve
    "She looks crestfallen, her face frozen in anguish. As she approaches you in the queue, she perks up a great deal."
    sarah happy "Marcy! You're serving today? You make a pretty lunch person, haha."
    "You serve her ramen with the chopped ham, and she cradles the bowl in her hands, as if it were a precious treasure."
    sarah happy "Thank you!"
    show sarah worried
    "As she moves away, Sarah's gaze falls once more, the joy draining from her face. Did something happen?"
    jump day2_end

label day2_sarah:
    show marcy neutral at left_side with dissolve
    show sarah neutral at right_side with dissolve
    "Sarah beams when she sees you."
    sarah happy "Marcy! I'm so glad you're here - I need your help!"
    "She takes you by the wrist and brings you to the Basement with her without further say."
    scene bg basement with fade
    show marcy uneasy at left_side with dissolve
    show sarah happy at right_side with dissolve
    marcy uneasy "Wait, I have to—"
    show sarah neutral2 at right_side with dissolve
    "Before you can get another word in, Sarah’s grip on your wrists tighten almost painfully."
    show marcy smile at left_side with dissolve
    "You wince a bit before sighing resignedly, your vision filling with Sarah."
    marcy smile "Your ponytail bounces when you walk."
    show sarah happy at right_side with dissolve
    "Sarah scoffs, but laughs anyways."
    "She brings you to a stool before an easel and a plain white canvas."
    sarah happy "I asked around and NO ONE wanted to be my reference for a painting today. You are my only hope! I promise it won't be a painting of you - I just need your form."
    menu:
        "You paint here? Does Eleanor allow this?":
            sarah worried "I... I don't know, actually. But I found these supplies just collecting dust."
            sarah happy "I think the Aeuternum could use a new painting, don't you think? I used to paint a lot back in high school."
            $ bad_choice_count += 1
        "Yeah, I can be a reference for you. What are you trying to paint?":
            sarah happy "Sweet! I'm trying to create a symbolic painting of sorts - something to appreciate Forever and her lovers."
            sarah worried "Something better than just bread or flowers."
            sarah happy "I think Aeuternum could use the spirit of an artist."
            $ good_choice_count += 1
    if sarah_count >= 1:
        scene bg day2 sarah1 with dissolve
    else:
        scene bg day2 sarah2 with dissolve
    "You take your seat onto the stool. Sarah sighs in contentment."
    sarah happy "Thank you, I appreciate your help!"
    "She begins to focus on you as she takes her seat on the opposite side of the canvas, beginning to brush away carefully."
    menu:
        "I don't have to take my clothes off, do I?":
            "Amused, you watch as Sarah puffs up a bit, clearly flustered."
            sarah happy "Pfft! No, you are fine just the way you are. It would certainly improve this portrait, though..."
            "She laughs."
            "You mirror her laugh with your whole chest—when was the last time you did that?"
            marcy smile "Really now?"
            "Sarah rolls her eyes, clicking her tongue, then goes back to painting. The moment passes, but for the next several minutes a faint, but fond smile remains on your lips."
            "It’s so small, some would say it’s not there at all, but you feel Sarah’s gaze burning into you."
            "Just as you start to squirm a bit, you notice Sarah’s expression shift."
            $ good_choice_count += 1
        "When do you think you'll finish? I don't want to get into trouble.":
            sarah worried "Is it really that bad of an idea..? Let's just see, first. I can't go back now..."
            sarah happy "But don't worry! I'll wrap this up soon. Thanks again for being here."
            $ bad_choice_count += 1
    show bg basement with dissolve
    show marcy neutral at left_side with dissolve
    show sarah happy at right_side with dissolve
    "After putting the finishing touches to her painting, Sarah wipes off sweat from her brow."
    sarah happy "Phew! It looks amazing! Thanks so much, Marcy! I'll go and show this to Ele—"
    show sarah worried
    "Sarah stops dead as she witnesses something shining under one of the shelves. She brings it up to her, hints of dry blood on the hilt, and looks at you."
    sarah worried "What… is this?"
    show marcy uneasy at left_side with dissolve
    "You falter, taking a half step back. The object seems familiar, like you’ve seen it in passing before, but your memory is hazy."
    "Your head pulses in pain as you try to jog your memory, but Sarah is looking at you expectantly, clearly disturbed. You notice her hands shake, and you want to snatch the dagger from her hand, but your body stills."
    menu:
        sarah worried "The blood is dry but… it can’t be too old. Do you think this is used often?"
        "I... I don't know. Ask Eleanor?":
            sarah terrified "But what if Eleanor is the one using this? I guess I could ask her..."
            sarah worried "No, I'll put it back, I'm sure it's nothing crazy."
            "Sarah sets the knife back cautiously, shaking off her unease."
            $ good_choice_count += 1
        "You should hold onto it just in case. Something doesn't feel right about it.":
            sarah worried "Maybe I should. I don't know whose blood is on this, but I'll wipe it down. I hope no one is getting hurt."
            "Sarah slips the knife into her pocket, despite her unease."
            $ bad_choice_count += 1
    show marcy uneasy at left_side with dissolve
    sarah neutral "Let's not dwell on this - come on, I'm hungry! Let's go to get lunch."
    marcy uneasy "Wait, Sarah—"
    "You get a sense of déjà vu of just a few hours ago when Sarah was ushering you off to the basement. Sarah is already walking back, looking back at you with the same bright smile on her face."
    "Though you’re not one to disturb easily either, you’re not sure how she can snap back as if nothing happened. The mental image of Sarah grinning so happily after holding such a grim object sends a slight chill down your spine."
    scene bg black with fade
    "You go to the dining hall with Sarah and spend your dinner hour there, laughing with her."
    scene bg dining with fade
    "Tonight's menu is pot roast. It was slightly overcooked, a little under-seasoned - but it was warm and fragrant. It reminded you of home."
    jump day2_end

label day2_end:
    scene bg dining with fade
    "You eventually take a glass of wine as a routine end to the day."
    "You swish the dark drink around in the cup, examining its contents."
    "Something is… different about it lately. This happens every so often, the flavor of the wine changing suddenly with no mention. You would normally brush it off but you feel more attuned than usual lately."
    play music "music/uneasy_ambience.mp3"
    scene bg hallway with fade
    show marcy neutral at left_side with dissolve
    "On the way to your bedroom, you hear the thudding of heavy footfalls approaching."
    show sarah cry at right_side with dissolve
    show sarah cry at offscreen_left with move
    hide sarah with dissolve
    show eleanor cold at right_side with dissolve
    "The day ends with you on your way to the bedroom when you hear the sound of thumping, catching Sarah trying to run past you in a cry."
    show marcy uneasy at left_side with dissolve
    "You see Eleanor striding in her direction soon after, carrying a ruler in one hand. You hear the distant cries of Sarah as, presumably, Eleanor catches up with her nonchalantly."
    "Your limbs twitch to follow and stop them, to see what is happening - what Sarah could have possibly done - but you are overcome by the fear of being involved."
    show eleanor cold at offscreen_left with move
    hide eleanor with dissolve
    scene bg black with fade
    "Before you even realize it, you’ve carried yourself back to your room."
    scene bg bedroom with fade
    "You've done nothing, yet can't help but feel you've managed to cause this somehow..."
    "You rest the night."
    stop music fadeout 1.0

    if good_choice_count > bad_choice_count:
        $ good_day_count += 1
    else:
        $ bad_day_count += 1
    jump day3
