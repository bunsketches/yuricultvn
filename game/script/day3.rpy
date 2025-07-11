label day3:
    # Reset good and bad choice counts to 0
    $ good_choice_count = 0
    $ bad_choice_count = 0
    $ eleanor_bad_day3 = False
    $ sarah_bad_day3 = False
    scene bg sunrise with fade
    play sound "sfx/rooster.mp3"
    play music "sfx/forest.mp3" fadein 1.0
    "You wake up with a guilty lump in your throat. Dread sits at the bottom of your stomach."
    "The scar on half your body burns, your arm twitching in what registers to your body as pain, but what you know in your brain is not really there. The image of last night plays in your mind over and over and over again."
    "You can't shake the feeling of inevitable doom. You lay there for a while, with that terrible weight, before slipping out from the covers."
    "Your morning routine passes without issue, clockwork as usual. As always, you stand before Forever for morning prayer."
    if secret_end_progress >= 2:
        "A spiderweb of hairline cracks run all over the idol, with a particularly large crack slashing Forever's serene visage, revealing the hollow interior."
        "Was it always cracked like this?"
    "Your face appears in the scrying mirror by the candlelight, as you gather your thoughts."
    show marcy neutral at left_side with dissolve
    $ renpy.music.set_volume(0.25, 0.0)
    menu:
        marcy "What should I pray for?"
        "Offer your praise to the altar":
            "You kneel before the altar again. You rest your head into your lap before the statue."
            marcy neutral "I will always be with you, Forever. Take me when you are ready. I am here, and I will continue to be here for you."
        "Pray for yourself":
            marcy neutral "If you are there... I have a feeling, deep down, that something will happen today. I'm not sure what, but please protect me."
            $ secret_end_progress += 1
        "Do not pray":
            marcy neutral "This place is so fucked, I know it is."
    scene bg outside with fade
    show marcy neutral at left_side with dissolve
    "You exit the shed, to be greeted by the day, muted by heavy clouds. Something else hangs heavy in the air, a feeling that something is wrong."
    marcy "All right, time to get to it then."
    menu:
        marcy "What should I take care of today?"
        "The garden":
            "You spend the afternoon trimming roses, picking weeds, and occasionally taking breaks and taking in the breeze from standing under a hot sun."
            "You watch as the other members shape the hedges or water the plants. As the sun fell below the trees, you catch the silhouette of Sarah walking by."
            $ sarah_count += 1
            jump day3_sarah
        "The river":
            "You spend the afternoon leaning by the river, making an attempt at catching fish but failing horribly. You're soon content to watch others spearing rainbow trout with effortless skill."
            "You wrap up the day by packing the fish into a large cooler. While securing the cooler with straps, you catch the silhouette of Sarah in the distance - alone, pacing."
            "You find yourself gravitating toward her across the river."
            $ sarah_count += 1
            jump day3_sarah
        "The dining hall":
            "You are wiping the tables and mopping the floors of the dining hall after the lunch rush."
            "Suddenly, Eleanor suddenly appears, taking a seat at the bench beside you. She addresses you coolly, with the hard edge of command."
            eleanor happy "Come, sit."
            $ eleanor_count += 1
            jump day3_eleanor
        "The kitchen":
            "You do ingredient prep and cook dishes all day. Sarah serves food out front - too engaged with the hungry crowd for you to interact."
            "When the lunch rush wraps up, you step out - splashing water into your face at a nearby bucket."
            "As you pat your face dry with your shirt, you catch the silhouette of Sarah briskly walking out of the back door."
            $ sarah_count += 1
            jump day3_sarah
        "The hallways":
            "You dust the halls for hours. You concentrate on a bookshelf when a hand snakes up onto your shoulder. You whirl around, finding Eleanor with her lips curled gently."
            $ eleanor_count += 1
            jump day3_eleanor
        "The basement":
            "You are changing a lightbulb in the Basement, perched precariously on a rickety stool, screwing in the new bulb into the light fixture."
            "As the light flickers back to life, it suddenly reveals Eleanor standing before you."
            "Startled, you stumble off the stool, but Eleanor is there to catch you."
            "She sets you down onto your feet, a dark shade filling her eyes as she locks them into yours - the knowing look of a predator, and you are her prey."
            $ eleanor_count += 1
            jump day3_eleanor

label day3_eleanor:
    scene bg background2
    "You've known Eleanor long enough to know that look, those dark eyes, the scheme lurking behind them."
    "And that smile tells you it's something she is excited about and very sure of."
    menu:
        eleanor happy "Working hard today, Marcy?"
        "Very. And I'm looking forward to relax today - I could use it.":
            eleanor happy "I understand. You can relax later, I assure you. I wont take too much of your time."
        "Not nearly hard enough - I feel like there is more I could do.":
            eleanor happy "There is more you can do. Let me show you."
        "I guess? I'm just doing what I need to.":
            eleanor happy "Thank you for that, Marcy."
    "Eleanor takes your hand."
    eleanor happy "Come with me."
    "You can't help but follow her as she leads you on."
    "You arrive at the basement, where she opens a hidden door leading to a secret room."
    "In this hidden chamber, a large version of Forever's statue stands proudly. Before the statue waits an altar with a red altar cloth."
    "There is a silver, intricately engraved ornamental knife resting on top of it, which seems familiar."
    if saw_knife:
        "You recognize this knife."
    "Barrels of wine decorate the room, and a row of silver chalices hang from a rack on the wall."
    "You drank from a chalice every night - didn't ask questions about the wine - but now that you're here, you force the thought out of your mind on what this implies."
    "Eleanor has her hand at your shoulder again as she gestures to the room."
    eleanor "Look upon this, where my work is done. This is where we keep our bonds with Forever. This is where the magic is - where Her love is, in its purest form."
    eleanor "Where we drink of Her."
    "She holds your hands in her own, turning to you - giving them a squeeze. A lean hunger glimmers in her crazed eyes, like the glint of knives in a dark alley."
    eleanor "Join me. Become great with me. Let's meet Forever together, and be her Chosen."
    "The fanatic edge in her voice is like diamond: cold, hard, and clear."
    eleanor "You have this one chance, Marcy - your potential is unfathomable. Together, we'd be unstoppable."
    eleanor "I feel so sure of myself when I see you - we were meant to be, Marcy. Imagine what we can bring."
    menu:
        "Eleanor, this is crazy! Are we sacrificing people and drinking their blood? That's insane!":
            eleanor "They sacrifice themselves, for Her. For our goddess and her love eternal. We drink their thanks in Her name."
        "What are we doing with the altar? What's with the knife?":
            eleanor "I will show you later. We will do it together. Sarah, the hardworking and loving girl she is, will be perfect. Let me walk you through this."
        "Let's do it.":
            "Purpose. The offer races through your veins, sparking a flame in your heart."
            eleanor "Marcy, I love you. I have looked forward to this - thank you."
            eleanor neutral "I'll make the announcement. We will drink to your promotion."
            jump day3_end
    menu:
        eleanor "Will you join me, Marcy? Can you trust me, please?"
        "Okay, I'll do it.":
            "You don't know what you're doing, but you close your eyes and breathe."
            eleanor "Marcy, I love you. I have looked forward to this - thank you."
            eleanor neutral "I'll make the announcement. We will drink to your promotion."
        "There has to be a better way...":
            marcy neutral "I can't do this, Eleanor. I'm sorry. This isn't right."
            "Something snaps in Eleanor's eyes, and her face stills, emotion draining from it. She lets you go."
            eleanor neutral "So be it."
            "She then shoves you to the altar and grabs the knife in an attempt to stab you."
    if good_choice_count > bad_choice_count:
        $ eleanor_bad_day3 = True
    jump day3_end

label day3_sarah:
    scene bg background2
    "You approach Sarah, finding her in distress. Bags hang from under her eyes - her hair disheveled."
    marcy neutral "Sarah?"
    "Sarah gasps as she sees you."
    sarah neutral2 "Marcy! What are you doing here?"
    marcy neutral "Chores. I saw you passing by. Is everything okay? I heard you last night... and Eleanor. What happened?"
    "Sarah sighs.  She smooths her hair, chuckling - and you hear notes of hysteria in that laugh, as if a part of her fell off a ledge inside."
    sarah neutral2 "Nothing happened. Just..."
    sarah neutral "I'm not good enough for this place, I guess."
    menu:
        "Did Eleanor tell you that?":
            sarah neutral "Something like that... But it's okay."
        "Then you should consider trying harder.":
            marcy neutral "Sarah, you're so... different from the others. You should tone it down."
            sarah neutral "Oh."
    "Sarah rubs her arm."
    sarah neutral "Marcy, I..."
    sarah happy "I just want to say thanks, for being a friend. I really think you're cool. I'm sorry if I made things weird - if I'm weird. I didn't mean for you to see me like this."
    menu:
        "It's not weird at all.":
            sarah happy "Come with me."
            "Sarah takes you to the Garden - holding your wrist the same way she had dragged you playfully the other day."
            "You feel warm inside - like you've found something worth holding onto, that's beyond Forever and this toxic place."
        "You need to get out of here.":
            marcy neutral "You should leave, tonight. This is not the place for you. I don't want you to get hurt by staying here."
            sarah neutral2 "Yeah... Maybe I should."
            sarah neutral "I hope you find the strength to leave this place someday, too."
    if good_choice_count > bad_choice_count:
        $ sarah_bad_day3 = True
    jump day3_end

label day3_end:
    scene bg background3
    marcy "This is the end of Day 3. We will compare how many good and bad choices for were made for this day."
    if good_choice_count > bad_choice_count:
        "Looks like we made more good choices than bad. Today was a good day!"
        $ good_day_count += 1
    else:
        "Looks like we made more bad choices than good. Today was a bad day!"
        $ bad_day_count += 1
    marcy "Now we'll jump to the ending..."
    jump end
