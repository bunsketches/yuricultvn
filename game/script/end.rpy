label end:
    default end_string = ""
    if eleanor_count > sarah_count:
        $ end_string = "eleanor"
    else:
        $ end_string = "sarah"
    if good_day_count > bad_day_count:
        $ end_string += "_good"
    else:
        $ end_string += "_bad"
    jump expression end_string

label eleanor_good:
    if eleanor_bad_day3:
        scene bg black with fade
        "Your heart beats wildly in your chest, from what you tell yourself is… fear? You’re not sure where Sarah is, and while you hope she escaped, given the situation you assume the worst."
        show marcy devastated at left_side with dissolve
        show eleanor psychotic at right_side with dissolve
        "Eleanor slowly walks toward you, a crazed look on her face. Everything in you tells you to run, to fight, to scream, to do something."
        marcy angry "G-Get away! S-Stop this!"
        "Eleanor laughs; Though you wanted to be genuine in your warnings, your own voice betrays you, and Eleanor is very aware of this."
        marcy uneasy "P-Please…"
        "Eleanor steps even closer, and suddenly she fills your space. All you can see is Eleanor. All you can think about is Eleanor, {i}Forever{/i}. You feel your inhibitions slip away as the tenseness from your body fades, replaced by want."
        scene bg black with fade
        "You want to give in."
    scene bg background1
    "Eleanor kisses you as you sacrifice Sarah together with the sacrificial dagger over an altar in the basement."
    "You both wield it together by its hilt as if you are a married couple. You are cheered on by surrounding cloaked cult followers, holding up chalices for Sarah's blood."
    return

label eleanor_bad:
    if eleanor_bad_day3:
        scene bg black with fade
        "Your heart beats wildly in your chest, from what you tell yourself is… arousal?"
        show marcy uneasy at left_side with dissolve
        show eleanor happy at right_side with dissolve
        "Eleanor leans in, kissing you sweetly before drawing back. She brings the cup of “wine” to your lips."
        "Though you wait eagerly, as soon as the taste of it finally registers as iron after all this time, you cough."
        show marcy devastated at left_side with dissolve
        show eleanor psychotic at right_side with dissolve
        "Sputtering, you shove her away."
    scene bg background1
    "You wrestle with Eleanor over the altar - and pin her. Fear races into Eleanor's eyes."
    eleanor neutral "Marcy, wait - I'm sorry-!"
    "You jab the knife into her leg. With her incapacitated, you close the secret room on Eleanor and lock it."
    return

label sarah_good:
    if sarah_bad_day3:
        scene bg black with fade
        "You watch as Sarah begins to walk off again. Images of Sarah’s terrified look as she runs through the hallway flash in your mind. It’s not right for Sarah’s smile to be tarnished like that. You  won’t let it happen again."
        marcy uneasy "Wait!"
        show sarah neutral2 at right_side with dissolve
        "Sarah turns around, clearly not expecting you to speak up."
        show sarah happy at right_side with dissolve
        "Soon enough elation overtakes her and she smiles, grabbing your wrist."
        sarah "Come on, then!"
    scene bg background1
    "Sarah takes you to a bench. You sit together, watching as the stars come out."
    show marcy neutral at left_side with dissolve
    sarah "The stars are comforting for me."
    marcy "Is there anything else comforting you?"
    sarah "Of course, silly..."
    sarah "You."
    "Without further words, you lean into each other - a moment without thinking."
    "You catch the gleam of something shiny as your eyes close."
    "You kiss. Although you are losing yourself in the moment, you can feel something warm spattering against you."
    "You look down to find blood - frightening amounts of it. So much. Too much."
    "Under the moonlight, you watch as Sarah holds up her severed forearm to you - eyes welling up with tears of love, pain and ecstasy."
    sarah "Eat of me..."
    sarah "Make me a part of you, for Her. I won't face this world without being a part of you."
    sarah "I will feel the love that you feel, so I can receive Her blessing. So I can be seen by Her."
    marcy "I love you, Sarah."
    sarah "Thank you." 
    "You watch as she drifts with the arm in her right hand. She cries as you take it, gripping your shirt to soothe herself from the pain."
    "You take her arm, and slowly... for Forever's sake, start biting into it."
    "Just one swallow of her, as you cradle the rest of Sarah in your arms while she dies."
    "Sarah passes from the world with her tears drying and a smile of relief on her face."
    return

label sarah_bad:
    if sarah_bad_day3:
        scene bg black with fade
        "As you approach a bench in the garden, you feel a painful headache come on. Images of Eleanor, her voice, her footsteps as she chases Sarah all cloy at your head."
        "Your ears begin to ring. Your legs begin to feel like they’re trudging through mud."
        show sarah worried at right_side with dissolve
        "Sarah notices your change in pace, and turns to look at you."
        "You try to find the words, but Sarah speaks up before you can."
        sarah cry "I… think I understand."
    scene bg background1
    "Sarah begins to turn for the woods."
    sarah neutral "Goodbye, Marcy."
    "She walks away, leaving you, Aeuternum, and Forever behind."
    return
