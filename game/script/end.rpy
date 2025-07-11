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
    scene bg garden3
    show marcy concern at left_side with dissolve
    show sarah happy at right_side with dissolve
    "Sarah takes you to a bench, patting the spot beside her.  You sit together, watching as the stars come out."
    show sarah neutral at right_side with dissolve
    "You watch together in silence for a moment. It’s peaceful in a way that  Aeuternum has never been before. Sarah opens her mouth to speak, her voice smaller than her usual tone."
    sarah "I’ve always liked stars. They’re…comforting for me."
    show sarah happy at right_side with dissolve
    "You turn your head, looking at her while her eyes are still fixed on the twinkling lights above."
    marcy "Is there anything else comforting you?"
    "Sarah tears her eyes away from the night sky for the first time since sitting down. She looks at you fondly, hope behind her eyes."
    sarah "You."
    "Without thinking, you silently lean in toward Sarah, and you briefly get a glimpse of Sarah doing the same."
    "You catch the gleam of something shiny before your eyes close."
    "You share a tender but brief kiss under the stars. You’re still pressed against Sarah when you feel something warm sputter at your side."
    show marcy uneasy at left_side with dissolve
    "You look down to find blood - frightening amounts of it. So much. Too much."
    "Under the moonlight, you watch as Sarah holds up her severed forearm to you - her eyes welled up with tears inextricably mixed with love, pain and ecstasy."
    sarah "Eat it."
    sarah "Make me a part of you, for Her. I won’t face this world without being a part of you."
    sarah "I will feel the love that you feel, so I can receive Her blessing. So I can be seen by Her."
    "You are stunned into silence, so when you don’t respond, Sarah continues rambling on."
    sarah "Please, Marcy. I want you to, I promise."
    sarah "I think this is what Eleanor wanted. I can feel it. This is it."
    sarah "This is what she taught me last night, do you remember? You ran, but I knew you just wanted me to learn."
    sarah "My Ultimatum."
    sarah "My Love."
    sarah "For Her, for Forever, for you, Marcy."
    sarah "It’s only been a few days, but I want you to see me. More than anything. So please… Eat it."
    "You gulp, though your throat is still dry. Before you can even process what’s happening, you blurt out—"
    marcy "I love you, Sarah."
    "Sarah smiles, her eyes flooding with joy."
    sarah "{i}Thank you{/i}."
    "You watch as she drifts with the arm in her right hand."
    "For a moment, it seems like she might fall over, but she quickly corrects her posture."
    "She cries as you take it delicately, gripping your shirt to soothe herself from the pain."
    "You can hear her wince, and you think to yourself that the sound was a bit cute."
    scene bg garden3 with fade
    "You take her arm, and slowly… for Forever’s sake, sink your first bite into it."
    "Your teeth tear through it as if it was your regular dinners that you would’ve shared with Sarah just a few hours ago. Bile starts to build in your throat as you chew."
    "After what seems like Forever, you swallow as you cradle the rest of Sarah in your arms feeling her body go cold."
    "Sarah passes from the world with her tears drying and a smile of relief on her face, below her beloved starry night sky."
    "As you watch the warmth drain from your lover, you take another look at the dismembered arm in your grasp."
    "The bile in your throat turns into desire, and before you can have second thoughts, you bite down."
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
    "Sarah begins to turn for the woods. The moonlight is a spotlight for her form before the gaping cavern created by the looming trees. She looks beautiful."
    if sarah_day3:
        sarah "Thanks for watching the stars with me, Marcy."
    "You look at Sarah’s back turned toward you, but Sarah turns her head to look at you one last time. For once, she has no words."
    "You want to say something, say that you wished you could’ve helped her, beg to go with her."
    "But again, you feel stuck in place, your feet refuse to step forward, and your mouth is dry."
    "And again, your throat is dry. You know she is going to leave and that you’re never going to see her again."
    "Sarah begins to turn for the woods."
    marcy concern "Goodbye, Sarah."
    "Sarah looks shocked for a moment, as if she didn’t expect you to let go that easily."
    "Still, she fixes her smile as always. You hope, so deeply, that she says something. That she’ll laugh again and say she’s kidding, skipping back to you. But nothing comes."
    "With that, Sarah finally walks off into the dark woods."
    scene bg sunrise with fade
    "You are left to wonder what “it” is forever as you live out your days in Aeuternum without Sarah."
    scene bg house2 with fade
    "Your days are filled with the same monotonous cycle again."
    scene bg dining with fade
    "Wake up, chores, eat, and drink until you pass out and do it all over again."
    scene bg garden3 with fade
    "Sometimes, you wander off to the garden again at night, hoping to see the stars just one more time."
    "They’re never there, though, and neither is Sarah."
    scene bg bedroom with fade
    "A few weeks later, you overhear Eleanor in her quarters as you’re about to go to bed. She’s on the phone, seemingly questioned about local disappearing people, and Eleanor replies so calmly, so trained."
    scene bg black with fade
    "So collected, so independent. So unlike Sarah."
    return
