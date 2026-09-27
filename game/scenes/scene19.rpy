# this scene is tricky. breakdown of the dialogue and lyrics:
# https://docs.google.com/document/d/1QdPX6fyZ_rFxAKN6Oh0Z_omihUI0GnhU271TUbYN0xU/edit?tab=t.0
label scene19: 
    # > 19       INT. THE SPACESHIP EDEN MAIN DECK                                        19
    scene bg spaceship window:
        matrixcolor BrightnessMatrix(0.2)
    # scene bg spaceship window
    show layer master at fx.flashback
    show gunner at left, flip
    show officer at right, noflip
    show navigator at right2, noflip
    # show kohei neutral at left2:
        # matrixcolor BrightnessMatrix(0.1)
    show kohei serious 1 at left2
    with dissolve

    call say_song_line(song_finalday, 0)
    # come don the mask... rivals I prevail
    call say_song_line(song_finalday, 1)

    gunner "Captain, beam array at 60 percent and climbing; Firing window opens in 3 minutes and counting."
    kitadani "Copy that, thank you Gunner Chief. Navigation, a read on the firing zone."
    navigator "Target is in optimal range, blast zone is clear of any civilian ships. No satellites, natural or otherwise."

    # beat the fart of sabik
    call say_song_line(song_finalday, 2)
    officer "Captain, I have the secure line ready."
    kitadani neutral "Give me just a second."
    gunner "70 percent."
    navigator "We’re holding steady Captain. Go take your call."
    # beat the fart of sabik
    call say_song_line(song_finalday, 3)
    # witness ultima... rise ultima
    call say_song_line(song_finalday, 4)

    # > GUIDE US OH MIGHTY FURY...
    #
    # Removed this dialogue: https://discord.com/channels/1307031043915911278/1308533742209335336/1551602844627378280
    # "cc @Evan Rosson thanks to Illy I remembered that we didn't have this written down anywhere. My bad: so the Usagi line during Final Day should be gone."
    #usagi postgrad neutral focus "On that day, I remember my mom holding for him, our bags were packed and we were ready to go..."
    #usagi postgrad neutral focus "Our society had decided that it was going to defy nature itself. We were about to learn a great lesson."

    gunner "80 percent! We’re closing in on the window."
    ### page 35 ###
    navigator "Holding steady."
    kitadani serious 1 "I’ll take the call in my quarters. First officer, you have the conn."
    # > Rhos an kyn ala na...
    officer "Aye Captain. I have the conn."

    # kohei leaves the room for a moment...
    # this scene moves fast - gotta animate the characters fast too
    show kohei:
        xoffset 0
        ease 0.5 xoffset -800
    show officer:
        alpha 0
    show gunner:
        alpha 0
    show navigator:
        alpha 0
    pause 0

    show bg spaceship window:
        matrixcolor BrightnessMatrix(0.2)
    show bg spaceship window
    show kohei worried at center, flip:
        xoffset -1000
        ease 0.5 xoffset 0
    with fade
    kitadani "Just listen to me. I want you and Usagi to take move to our spot in the moon barracks-"

    # guide us o mighty fury... to victory
    call say_song_line(song_finalday, 5)
    # justice no forgiveness... final sentence
    call say_song_line(song_finalday, 6)
    # dys an sohm in... ala na da da da (overlaps)
    kitadani "I know it was supposed to be a few more years, but... But this doesn’t look good. If what Barry said is true... Just go... I have to get back now. I love you."

    show kohei worried at center, noflip:
        xoffset 0
        ease 0.5 xoffset -1000
    pause 0

    show bg spaceship window:
        matrixcolor BrightnessMatrix(0.2)
    show gunner:
        alpha 1
    show officer:
        alpha 1
    show navigator:
        alpha 1
    with fade
    show kohei serious 1 at left2, flip:
        xoffset -800
        ease 0.5 xoffset 0

    officer "Captain on Deck"
    gunner "90 percent!"
    show kohei serious 2
    navigator "Captain, a development. The Crystal is... opening."
    kitadani "Then this is our chance. That... thing... is coming out again and this time it means to kill us all."
    gunner "100 percent! The firing window is open."

    # > Gunner Chief locks and loads the Ultima Canon.
    kitadani panic 2 "Ready the Ultima Cannon!"

    # now breathe deep... beneath the flood
    call say_song_line(song_finalday, 7)
    kitadani serious 3 "Today we stand ready to defend all that we hold dear. Our families, our friends, our neighbors and our planet."
    # where all of the proud angels... dreams they've spun (overlaps with kitadani's speech)
    call say_song_line(song_finalday, 8)
    # yet ever we still... invincible
    call say_song_line(song_finalday, 9, last=True)

    ### page 36 ###
    ### <manga-panels> ###
    # manga panels: fighting the planet destroyer
    window hide
    window auto
    scene bg white with dissolve
    show bg white as bg2 behind bg
    show bg scene19 1 with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    call fx.log("Singing continues, but no more lyrics are displayed.")
    call fx.log("Dialogue is NOT in the usual subtitles, but in onscreen manga. Listen to dialogue for when to click:")
    call fx.log("PD: \"Behold, I am come. I am the beginning and the end\"")
    call fx.log("Officer: \"Captain!\"")
    call fx.log("Kitadani: \"Steady!\" <CLICK>")
    pause

    show bg scene19 2 with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    call fx.log("Navigator: \"The PLANET DESTROYER is emerging from the crystal!\"")
    call fx.log("Gunner: \"Captain, on your command!\"")
    call fx.log("Kitadani: \"Fire!\"")
    call fx.log("REST: \"AAAAHHHHHHHH\" <CLICK>")
    pause

    show bg scene19 3 with dissolve:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 0.8
        linear 10 zoom 1.0
    call fx.log("Gunner: \"Impact!\"")
    call fx.log("Navigator: \"The field is not clear, the Planet Destroyer, it-\"")
    call fx.log("Officer: \"It absorbed the blast...\" <CLICK>")
    pause

    show bg scene19 4 with dissolve:
        # TODO different bg on this one
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.0
        #linear 10 zoom 1.0
    call fx.log("Gunner: \"Brace for counter-attack!\"")
    call fx.log("Kitadani: \"Ready another blast!\"")
    call fx.log("REST: \"AAAAHHHHHHHH\" <CLICK>")
    pause

    show bg:
        yshake(5, 1000, 0.02)
    show bg neongreen as boom:
        alpha 0.0
        # pause 0.5
        linear 2.0 alpha 1.0
    call fx.log("(pause a moment, for effect)")
    pause

    scene bg black with dissolve
    call fx.log("(pause - continue when news reporters start talking)")
    pause
    #destroyer "Behold, I am come, I am the Beginning, And the End."
    #officer "Captain!"
    #kitadani "Steady!"
    #navigator "The PLANET DESTROYER is emerging from the crystal"
    #gunner "Captain on your command!"
    ## > Ecce venio
    #kitadani "FIRE!"
    #gunner "Impact!"
    #navigator "The field is NOT CLEAR, the planet destroyer it-"
    #officer "It absorbed the blast..."
    #gunner "Brace for counter attack!"
    #kitadani "Ready another blast!"
    ### </manga-panels> ###
    # > et principia!

    # > BLACK OUT, SCREEN REVEALS SHOW TITLE/ LOGO “OTAKU ORATORIO 2:
    # > I set out to save the world, but it turns out the world’s
    # > greatest threat is a kid who calls me mom.”
    # NOPE this was an old directive from when this was scene 1
    #scene bg beige
    #show logo:
    #    anchor (0.5, 0.5)
    #    pos (0.5, 0.5)
    #    zoom 0.5
    #with fade
    #pause

    window hide
    window auto
    $ y = 0.48
    scene bg news studio:
        noflip
        anchor (0.5,1.0)
        pos (0.5,1.0)
        zoom 1.15
    show layer master at fx.flashback
    show reporter1:
        zoom 1.0
        xpos 0.2
        ypos y
    show reporter2:
        zoom 1.0
        xpos 0.5
        ypos y+0.03
    show reporter3:
        zoom 1.0
        xpos 0.8
        ypos y
    # show bg breaking news as bg2:
        # ease 0.5 zoom 1.0
    # show fx_crt_scanlines
    with dissolve
    reporter1 "It is unclear whether or not the crew of the Eden are responding after that...."
    reporter1 "Wait... I’m getting word."
    ### page 37 ###
    reporter2 "It is confirmed, the planet destroyer has been neutralized completely."
    reporter3 "But the Space shuttle Eden and its crew has been decimated in the blast fall out."
    reporter3 "Folks at home, I think now is a time for a moment of silence as we think about the Eden and their sacrifice..."
    # > BARTHANDELUS STOPS THE FOOTAGE. HE HAS BEEN WATCHING THIS OLD
    # > CLASSIFIED RECORDING FOR SOME REASON....

    # transition to bart and tv in a dark room
    scene bg black
    show bg news studio as tv:
        anchor (0.5, 1.0)
        zoom 0.2
        left2
    show fx_crt_scanlines as tv2:
        anchor (0.5, 1.0)
        zoom 0.2
        left2
    show bart neutral focus at right2
    with irisin
    pause 2

    # bart turns off the tv
    show bg news studio as tv:
        linear 1 alpha 0
    show fx_crt_scanlines as tv2:
        linear 1 alpha 0
    pause 2

    # bart leaves
    show bart:
        flip
        xoffset 0
        easeout 2 xoffset 800
    pause 2
    return

# final day: https://drive.google.com/drive/folders/1T-gmJgYGuGVAJbqzP6_ts-XL2xaXKN_O
define song_finalday = Song(Character("The Final Day"), [
    Line("Come don the mask of blind betrayal\nE’er does the head devour its tail\nAs iron bends to steel\nO’er my rivals I prevail",
        "(This song has dialogue mixed in with the lyrics, and it moves FAST. I hope these comments help. Good luck.)",
        at_measure=3),
    Line("Beat the heart of Sabik\nThe heart of Sabik\nThe heart of Sabik",
        "(13 sec/9 m. of dialogue, until \"no sattelites natural or otherwise\", then...)",
        at_measure=29),
    Line("Beat the heart of Sabik\nThe heart of Sabik\nThe heart of Sabik",
        "(6 sec/4 m. of dialogue, until \"go take your call\", then...)",
        at_measure=37),
    Line("Witness Ultima\nWitness Ultima\nWitness, witness, witness, ahhhh!\nRise Ultima, ah!",
        at_measure=45),
    Line("Guide us, O mighty Fury\nGuide us to victory",
        "(16 sec/10 m. of dialogue, until \"move to our spot in the moon barracks-\", then...)",
        at_measure=70),
    Line("Justice, no forgiveness\nVengeance, no deliverance\nWitness to their trespass\nPass this final sentence",
        at_measure=79),
    # skip this line - subtitles for the draconic lines would be nice, but it overlaps with important dialogue
    # Line("Dys an sohm in\nan sohm in\nRhos ankyn ala na\nala na da da da",
        # at_measure=0),
    Line("Now breathe deep of the darkness beneath the flood...",
        "(41-43 sec/20 m. of dialogue, until \"Ready the Ultima Cannon!\", then...)",
        at_measure=107),
    Line("Where all of the proud angels drink to their deeds of blood\nTheir lies, twisted and torn, into dreams they’ve spun",
        "(Kitadani's speech, ending with \"our neighbors and our planet\". Speech overlaps w/ these lyrics - so click through quickly, probably!)",
        at_measure=111),
    Line("Yet ever we still stand tall\nNever we fall\nInvincible",
        "(Speech overlap ends, then...)",
        at_measure=119),
], num_measures=145)