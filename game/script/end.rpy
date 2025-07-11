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
    scene bg background1
    "Eleanor kisses you as you sacrifice Sarah together with the sacrificial dagger over an altar in the basement."
    "You both wield it together by its hilt as if you are a married couple. You are cheered on by surrounding cloaked cult followers, holding up chalices for Sarah's blood."
    return

label eleanor_bad:
    scene bg background1
    "You wrestle with Eleanor over the altar - and pin her. Fear races into Eleanor's eyes."
    eleanor neutral "Marcy, wait - I'm sorry-!"
    "You jab the knife into her leg. With her incapacitated, you close the secret room on Eleanor and lock it."
    return

label sarah_good:
    scene bg background1
    "Sarah takes you to a bench. You sit together, watching as the stars come out."
    sarah happy "The stars are comforting for me."
    marcy happy "Is there anything else comforting you?"
    sarah happy "Of course, silly..."
    sarah happy "You."
    "Without further words, you lean into each other - a moment without thinking."
    "You catch the gleam of something shiny as your eyes close."
    "You kiss. Although you are losing yourself in the moment, you can feel something warm spattering against you."
    "You look down to find blood - frightening amounts of it. So much. Too much."
    "Under the moonlight, you watch as Sarah holds up her severed forearm to you - eyes welling up with tears of love, pain and ecstasy."
    sarah happy "Eat of me..."
    sarah happy "Make me a part of you, for Her. I won't face this world without being a part of you."
    sarah happy "I will feel the love that you feel, so I can receive Her blessing. So I can be seen by Her."
    marcy happy "I love you, Sarah."
    sarah happy "Thank you." 
    "You watch as she drifts with the arm in her right hand. She cries as you take it, gripping your shirt to soothe herself from the pain."
    "You take her arm, and slowly... for Forever's sake, start biting into it."
    "Just one swallow of her, as you cradle the rest of Sarah in your arms while she dies."
    "Sarah passes from the world with her tears drying and a smile of relief on her face."
    return

label sarah_bad:
    scene bg background1
    "Sarah begins to turn for the woods."
    sarah neutral "Goodbye, Marcy."
    "She walks away, leaving you, the Barn, and Forever behind."
    return
