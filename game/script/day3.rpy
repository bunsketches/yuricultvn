label day3:
    # Reset good and bad choice counts to 0
    $ good_choice_count = 0
    $ bad_choice_count = 0
    $ eleanor_bad_day3 = False
    $ sarah_bad_day3 = False
    $ sarah_day3 = False
    $ eleanor_day3 = False

    scene bg sunrise with fade
    "You wake up with a guilty lump in your throat. Dread sits at the bottom of your stomach."
    play sound "sfx/rooster.mp3"
    play sound "sfx/forest.mp3" fadein 0.5 loop
    "The scar on half your body burns, your arm twitching in what registers to your body as pain, but what you know in your brain is not really there. The image of last night plays in your mind over and over and over again."
    "You can't shake the feeling of inevitable doom. You lay there for a while, with that terrible weight, before slipping out from the covers."
    "Your morning routine passes without issue, clockwork as usual. As always, you stand before Forever for morning prayer."
    if secret_end_progress >= 2:
        "A spiderweb of hairline cracks run all over the idol, with a particularly large crack slashing Forever's serene visage, revealing the hollow interior."
        "Was it always cracked like this?"
    "Your face appears in the scrying mirror by the candlelight, as you gather your thoughts."
    stop sound fadeout 0.5
    
    scene bg pray start
    marcy "What should I pray for?"
    menu:
        "Offer your praise to the altar":
            scene bg pray respects
            "You kneel before the altar again. You rest your head into your lap before the statue."
            marcy smile"I will always be with you, Forever. Take me when you are ready. I am here, and I will continue to be here for you."
        "Pray for yourself":
            scene bg pray yourself
            "You clasp your hands together tightly and bow your head down."
            marcy uneasy "If you are there... I feel it in me that something will happen today. I'm not sure what, but please protect me."
            "You linger for a moment before opening your eyes and running a hand down your face."
            $ secret_end_progress += 1
        "Do not pray":
            scene bg pray nothing
            "You look up, scowling at the statue's face."
            "You never noticed the small cracks adorning it, an imperfect surface as the object of everyone's unquestioning adoration."
            marcy uneasy "This place is so fucked, I know it is."

    scene bg outside with dissolve
    "As you move to walk away, you can't shake the feeling that something is wrong."
    "The statue's shadow looms over you even as you make a good bit of distance from it."
    show marcy neutral at left_side with dissolve
    marcy "All right, time to get to it then."
    marcy "What should I take care of today?"
    menu:
        "Trim the garden":
            show bg garden1 with dissolve
            "You spend the afternoon trimming roses, picking weeds, and occasionally taking breaks and taking in the breeze from standing under a hot sun."
            "You watch as the other members shape the hedges or water the plants."
            "As the sun falls below the trees, you catch the silhouette of Sarah walking by."
            $ sarah_count += 1
            jump day3_sarah
        "Catch fish by the river":
            show bg river with dissolve
            "You spend the afternoon leaning by the river, attempting to catch fish but failing horribly. You watch as the others nail rainbow trout under their stakes."
            "You wrap up the day by tying the fish up in a large cloth, and placing them into a chest."
            "While buckling the chest of fish, you catch the silhouette of Sarah in the distance - alone, pacing."
            "You find yourself gravitating toward her across the River."
            $ sarah_count += 1
            jump day3_sarah
        "Mop the dining hall":
            show bg dining with dissolve
            "After the lunch rush, you begin wiping down the table tops and mopping the dining hall floor."
            "After an hour or so of labor, you decide to sit down for a brief break, sighing."
            show eleanor cold at right_side
            "Suddenly, Eleanor appears. You hadn't even heard her footsteps."
            "You look up at her, unsure of what to say. She isn't normally seen out of her quarters at these hours."
            eleanor "Stand."
            $ eleanor_count += 1
            jump day3_eleanor
        "Meal prep in the kitchen":
            show bg kitchen with dissolve
            "You do ingredient prep and dishes all day. Sarah serves food at the front - too engaged with the hungry crowd to interact."
            "When the lunch rush wrapped up in the evening, you step out - splashing water into your face at a nearby bucket."
            "You pat it dry with your shirt, catching the dark shape of Sarah briskly walking out of the backdoor."
            $ sarah_count += 1
            jump day3_sarah
        "Dust the hallways":
            show bg hallway with dissolve
            "You dust the halls for hours. You concentrate on a bookshelf when a hand snakes up onto your shoulder."
            show eleanor cold at right_side
            "You whirl around, finding Eleanor with her lips curled gently."
            $ eleanor_count += 1
            jump day3_eleanor
        "Fix the basement lights":
            show bg basement with dissolve
            show marcy neutral at left_side with dissolve
            "You are changing a lightbulb in the Basement, perched precariously on a rickety stool, screwing in the new bulb into the light fixture."
            "The light flickers back on, revealing Eleanor standing in front of you. Watching."
            show marcy uneasy
            show eleanor cold at right_side
            "You flinch and topple off, bracing for impact."
            "It never comes as you feel Eleanor's arms wrap around you, catching you before you can hurt yourself."
            "She sets you down onto your feet, and fixes you a look—"
            "—That of the predator, and you are her prey."
            $ eleanor_count += 1
            jump day3_eleanor

label day3_eleanor:
    play music "music/eleanor_theme_day3.mp3" fadein 1.0 fadeout 1.0
    show marcy concern at left_side with dissolve
    $ eleanor_day3 = True
    "You've known Eleanor long enough to know that look, those dark eyes, the scheme lurking behind them."
    "And that smile tells you it's something she is excited about and very sure of."
    eleanor delighted "Working hard today, Marcy?"
    menu:
        "Very. And I'm looking forward to relaxing today - I could use it.":
            eleanor happy "I understand. You can relax later, I assure you. I wont take too much of your time."
            $ bad_choice_count += 1
        "Not nearly hard enough - I feel like there is more I could do.":
            eleanor happy "There {i}is{/i} more you can do. Let me show you."
            $ good_choice_count += 1
        "I guess? I'm just doing what I need to.":
            eleanor happy "Thank you for that, Marcy."
            $ bad_choice_count += 1
    "Eleanor takes your hand."
    eleanor happy "Come with me."
    "You can't help but follow her as she leads you on."
    "You arrive at the basement, where she opens a hidden door leading to a secret room."
    play sound "sfx/door_open.mp3"
    show bg basement2
    "In this hidden chamber, a large version of Forever's statue stands proudly. Before the statue waits an altar with a white altar cloth."
    "There is a silver, intricately engraved ornamental knife resting on top of it, which seems familiar."
    if saw_knife:
        "You recognize this knife, from when you and Sarah were in the basement."
    "Barrels of wine line the room, and a row of silver chalices hangs from a rack on the wall."
    "You drank from a chalice every night - didn't ask questions about the wine - but now that you're here, you force the thought out of your mind on what this implies."
    "Eleanor has her hand at your shoulder again as she gestures to the room."
    eleanor "Look upon this, where my work is done. This is where we keep our bonds with Forever. This is where the magic is - where Her love is, in its purest form."
    eleanor "Where we drink of Her."
    menu:
        "So that's why the wine tastes so...divine.":
            "Eleanor beams at you, perhaps the most genuine smile you've seen from her. She seems moved, proud even, as if she waited for this her whole life."
            eleanor psychotic "Yes, Marcy! Yes! That taste... we could have it {i}Forever.{/i} We just need to appease Her, and you know what She wants..."
            $ good_choice_count += 1
        "Her?":
            "Eleanor, once again, laughs at an inappropriate time. She thinks you're joking at a time like this."
            eleanor "Yes, Marcy... Her. We all want to appease her, right?"
            "Her eyes hold yours in a deadlock."
            $ bad_choice_count += 1
        "So all this time... the wine...":
            "Eleanor shakes her head, clicking her tongue, though for once she's not scolding you. She seems beyond her role as the leader at this point, and looks at you expectantly."
            eleanor "The wine is just the start, Marcy."
    show eleanor psychotic
    "She holds your hands in her own, turning to you - her grip is painfully tight. Her eyes light up, hungry, {i}craving{/i}."
    eleanor "Join me. Become {i}great{/i} with me. Let's meet Forever together, and be her Chosen."
    "Eleanor briefly turns to the altar to grab the dagger. When she turns, it cuts through the air audibly. Eleanor looks at you fanatically, almost trembling. You've never seen her ecstatic like this."
    eleanor "You have this one chance, Marcy - your potential is unfathomable. I've known it since we met all those years ago."
    "She lifts her hand up to touch your scarred cheek, and you swear you feel a searing burn."
    "Images of Eleanor from when you and her were younger now flash in your mind. When your flesh was still raw and when Eleanor still had a semblance of a real smile on her face."
    "You don't exactly pull away. You're not sure what's happening when your eyes close and you hum. Eleanor has always had that effect on others, but on you? Before you can dwell on the feeling, Eleanor begins speaking unevenly again."
    eleanor "Together, we'd be {i}unstoppable{/i}. I feel so sure of myself when I see you - we were meant to be, Marcy. {i}Imagine what we can bring{/i}."
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
    if good_choice_count > bad_choice_count:
        $ eleanor_bad_day3 = True
    jump day3_end

label day3_sarah:
    play music "music/sarah_theme_day3.mp3" fadein 1.0 fadeout 1.0
    $ sarah_day3 = True
    show marcy concern at left_side with dissolve
    show sarah terrified at right_side with dissolve
    "You approach Sarah, finding her in distress. Bags hang from under her eyes - her hair disheveled."
    marcy "Sarah?"
    "Sarah gasps as she sees you."
    sarah worried "Marcy! What are you doing here?"
    marcy "Chores. I saw you passing by. Is everything okay? I heard you last night... and Eleanor. What happened?"
    "Sarah sighs. She seems to go through a few different processes in her head as she composes herself."
    show sarah happy
    "She smooths her hair, chuckling - and you hear notes of hysteria in that laugh, as if a part of her fell off a ledge inside."
    sarah happy "Nothing happened. Just..."
    "Again, she falters, wincing. You wouldn't be surprised if Sarah could hold the world record for {i}Fastest Expression Change.{/i}"
    sarah cry "I'm not good enough for this place, I guess."
    menu:
        "Did Eleanor tell you that?":
            marcy angry "Did Eleanor tell you that?"
            sarah neutral "Something like that... But it's okay."
            "And there it is again. You suppose you're glad she's not as distressed anymore."
            $ good_choice_count += 1
        "Then you should consider trying harder.":
            marcy neutral "Sarah, you're so... different from the others. You should tone it down."
            sarah "Oh."
            "You awkwardly shift your weight around on either feet as Sarah bows her head down to sniffle a few more times."
            "However, as per usual, after a few beats pass she shakes her head and rises again."
            $ bad_choice_count += 1
    show marcy neutral at left_side with dissolve
    "Sarah rubs her arm."
    sarah "Marcy, I..."
    sarah "I just want to say thanks, for being a friend. I really think you're cool. I'm sorry if I made things weird - if {i}I'm{/i} weird. I didn't mean for you to see me like this."
    menu:
        "It's not weird at all.":
            marcy smile "Well, aside from trying to get me naked by 'painting' me."
            show sarah happy at right_side with dissolve
            "Sarah shoves your shoulder in what you assume to be a playful gesture, but you end up stumbling a few steps back. Damn, that girl is stronger than she looks."
            sarah "Oh my God! I told you that wasn't why!"
            "The laughter dies down and the moment breaks."
            show sarah worried at right_side with dissolve
            "Sarah looks at you, deadpan, for once her expression is hard to read, but only for a moment. Upon closer inspection, you see bags forming under her eyes that weren't there before."
            "Something is there."
            $ good_choice_count += 1
        "You need to get out of here.":
            show sarah worried at right_side with dissolve
            "She tilts her head at you, confused. You can practically see the dog ears drooping down above her head."
            marcy "This is not the place for you. I don't want you to get hurt by staying here."
            show sarah cry at right_side with dissolve
            "Clearly dejected, Sarah sighs loudly, rubbing at her wrists."
            sarah "Yeah... Maybe I should."
    show sarah happy at right_side with dissolve
    "Sarah wipes her tears."
    sarah "Thank you."
    show sarah neutral at right_side with dissolve
    "Sarah pauses for a moment. She looks up again with an eerie smile, looking at you and seemingly nothing else."
    sarah "I don't think I've felt so close to someone before. I really appreciate you."
    marcy uneasy "Sarah..?"
    sarah "Marcy, It's a big ask, but... Would you take something of mine? Take it with you, for the rest of your life?"
    menu:
        "Sure.":
            sarah happy "Awesome!"
            "She takes you to the Garden, guiding you by your wrist."
            show bg garden1 with fade
            show sarah happy at right_side with dissolve
            show marcy smile at left_side with dissolve
            "You feel warm inside, like you've found something worth holding onto, that's beyond Forever, beyond Aeternum."
            "You don't remember that 'beyond' part too well, but you feel you could probably get closer to that with Sarah. At least, you hope so."
        "I don't think I can.":
            show sarah cry at right_side with dissolve
            "A sadness grows in her eyes, and you hear her begin to sniffle again."
            sarah "Then that's everything... I hope you find the strength to leave this place someday, too."
    if good_choice_count > bad_choice_count:
        $ sarah_bad_day3 = True
    jump day3_end

label day3_end:
    if good_choice_count > bad_choice_count:
        $ good_day_count += 1
    else:
        $ bad_day_count += 1
    jump end
