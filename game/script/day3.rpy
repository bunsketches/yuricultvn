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
        "Very. And I'm looking forward to relaxing today - I could use it.":
            eleanor happy "I understand. You can relax later, I assure you. I wont take too much of your time."
            $ bad_choice_count += 1
        "Not nearly hard enough - I feel like there is more I could do.":
            eleanor happy "There is more you can do. Let me show you."
            $ good_choice_count += 1
        "I guess? I'm just doing what I need to.":
            eleanor happy "Thank you for that, Marcy."
            $ bad_choice_count += 1
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
    menu:
        "So that’s why the wine tastes so…divine.":
            "Eleanor beams at you, perhaps the most genuine smile you’ve seen from her. She seems moved, proud even, as if she waited for this her whole life."
            eleanor "Yes, Marcy! Yes! That taste… we could have it Forever. We just need to appease Her. And you know what She wants…"
            $ good_choice_count += 1
        "Her?":
            "Eleanor, once again, laughs at an inappropriate time. She thinks you’re joking at a time like this."
            eleanor "Yes, Marcy… Her. We all want to appease her, right?"
            "Her eyes hold yours in a deadlock."
            $ bad_choice_count += 1
        "So all this time… the wine…":
            "Eleanor shakes her head, clicking her tongue, though for once she’s not scolding you. She seems beyond her role as the leader at this point, and looks at you expectantly."
            eleanor "The wine is just the start, Marcy."
    "She holds your hands in her own, turning to you - giving them a squeeze. Her eyes light up, hungry, {i}craving{/i}."
    eleanor "Join me. Become {i}great{/i} with me. Let's meet Forever together, and be her Chosen."
    "Eleanor briefly turns to the altar, grabbing the dagger from the altar. When she turns, it cuts through the air audibly. Eleanor looks at you fanatically, almost trembling. You’ve never seen her ecstatic like this."
    eleanor "You have this one chance, Marcy - your potential is unfathomable. I’ve known it since we met all those years ago."
    "She lifts her hand up to touch your scarred cheek, and you swear you feel a searing burn."
    "Images of Eleanor from when you and her were younger now flash in your mind. When your flesh was still raw and when Eleanor still had a semblance of a real smile on her face."
    "You don’t exactly pull away. You’re not sure what’s happening when your eyes close and you hum. Eleanor has always had that effect on others, but on you? Before you can dwell on the feeling, Eleanor begins speaking unevenly again."
    eleanor "Together, we’d be {i}unstoppable{/i}. I feel so sure of myself when I see you - we were meant to be, Marcy. {i}Imagine what we can bring{/i}."
    menu:
        "Eleanor, this is crazy! Are we sacrificing people and drinking their blood? That's insane!":
            eleanor "They sacrifice themselves, for Her. For our goddess and her love eternal. We drink their thanks in Her name."
            $ bad_choice_count += 1
        "What are we doing with the altar? What's with the knife?":
            eleanor "I will show you later. We will do it together. Sarah, the hardworking and loving girl she is, will be perfect. Let me walk you through this."
            $ bad_choice_count += 1
        "Let's do it.":
            "Purpose. The offer races through your veins, sparking a flame in your heart."
            eleanor "Marcy, I love you. I have looked forward to this - thank you."
            eleanor neutral "I'll make the announcement. We will drink to your promotion."
            $ good_choice_count += 1
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
            "And there it is again. You suppose you’re glad she’s not as distressed anymore."
            $ good_choice_count += 1
        "Then you should consider trying harder.":
            marcy neutral "Sarah, you're so... different from the others. You should tone it down."
            sarah neutral "Oh."
            "You awkwardly shift your weight around on either feet as Sarah bows her head down to sniffle a few more times."
            "However, as per usual, after a few beats pass she shakes her head and rises again."
            $ bad_choice_count += 1
    "Sarah rubs her arm."
    sarah neutral "Marcy, I..."
    sarah happy "I just want to say thanks, for being a friend. I really think you're cool. I'm sorry if I made things weird - if I'm weird. I didn't mean for you to see me like this."
    menu:
        "It's not weird at all.":
            marcy smile "Well, aside from trying to get me naked by “painting” me."
            show sarah happy at right_side with dissolve
            "Sarah shoves your shoulder in what you assume to be a playful gesture, but you end up stumbling a few steps back. Damn, that girl is stronger than she looks."
            sarah "Oh my God! I told you that wasn’t why!"
            "The laughter dies down and the moment breaks."
            show sarah worried at right_side with dissolve
            "Sarah looks at you, deadpan, for once her expression is hard to read, but only for a moment. Upon closer inspection, you see bags forming under her eyes that weren’t there before."
            "Something is there."
            # sarah happy "Come with me."
            # "Sarah takes you to the Garden - holding your wrist the same way she had dragged you playfully the other day."
            # "You feel warm inside - like you've found something worth holding onto, that's beyond Forever and this toxic place."
            $ good_choice_count += 1
        "You need to get out of here.":
            show sarah worried at right_side with dissolve
            "She tilts her head at you, confused. You can practically see the dog ears drooping down above her head."
            marcy "This is not the place for you. I don’t want you to get hurt by staying here."
            show sarah cry at right_side with dissolve
            "Clearly dejected, Sarah sighs loudly, rubbing at her wrists."
            sarah "Yeah... Maybe I should."
    show sarah happy at right_side with dissolve
    "Sarah wipes her tears."
    sarah "Thank you."
    show sarah neutral at right_side with dissolve
    "Sarah pauses for a moment. She looks up again with an eerie smile, looking at you and seemingly nothing else."
    sarah "I don’t think I’ve felt so close to someone before. I really appreciate you."
    marcy uneasy "Sarah..?"
    sarah "Marcy, It’s a big ask, but… Would you take something of mine? Take it with you, for the rest of your life?"
    menu:
        "Sure.":
            sarah happy "Awesome!"
            "She takes you to the Garden, guiding you by your wrist."
            show sarah happy at right_side with dissolve
            show marcy smile at left_side with dissolve
            show bg garden1 with fade
            "You feel warm inside, like you’ve found something worth holding onto, that’s beyond Forever, beyond Aeuternum."
            "You don’t remember that “beyond” too well, but you feel you could probably get closer to that with Sarah. At least, you hope so."
        "I don't think I can.":
            show sarah cry at right_side with dissolve
            "A sadness grows in her eyes, and you hear her begin to sniffle again."
            "Then that’s everything… I hope you find the strength to leave this place someday, too."
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
