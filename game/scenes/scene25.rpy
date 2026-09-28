# https://otaku-oratorio-2026-gallery.netlify.app/?t=princess&t=bart+young&t=huxtable+young&t=jojo+young&t=kohei+young&t=linda+young
label scene25:
    scene bg training room:
        zoom 1.1
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    show layer master at fx.flashback
    with fade
    # "TODO is this where we use the moba training map? If so, do I want character sprites (like most scenes), or animated dots on the map (like a game minimap), or both? Until I answer those fundamentals, this scene is deliberately barebones"
    # PUSH TEAM
    show bart mech young neutral flip    at left2,  fx.xoffset(-1200)
    show kohei mech young serious 1 flip at center, fx.xoffset(-1200)
    show jojo mech young neutral flip    at left,   fx.xoffset(-1200)
    # DEFENDERS
    show princess mech neutral           at right,  fx.xoffset(1200)
    show huxtable mech young neutral     at right2, fx.xoffset(1200)
    show linda mech young neutral        at center, fx.xoffset(1200)
    # "TODO add emotes for this scene, at least"

    # > 25       INT. TRAINING ZONE, INSIDE MECH                                          25
    wellington "Today’s training is a final lane push on the enemy base."
    
    # manually from the center camera
    show bg at fx.ease_xpos(1, 0.5, 0.55):
        matrixcolor TintMatrix('#ffffff')
        linear 1.0 matrixcolor TintMatrix(redteam_bg)
    show jojo at fx.ease_xoffset(1, -1200, 0)
    show bart at fx.ease_xoffset(1, -1200, 0)
    show kohei at fx.ease_xoffset(1, -1200, 0)
    wellington "Push team: Joseph Chen, you’re on auxiliary. Bartholemew Barthandelus... Support. Kohei Kitadani Ace."

    call scene25.camera_blueteam
    wellington "Defenders: Elizabeth Newark-"
    ### page 47 ###
    princess "That’s Princess Elizabeth Newark, thank you."
    wellington "......... Princess Elizabeth Newark, you’re on Auxiliary, Robert Huxtable, you’re on support and Ace is Linda Hudson."
    princess "Okay cousin!!"
    linda_young "Hey gurl hey."
    huxtable "Ladies... maybe we should pay attention."
    princess "Robert, if you don’t shut yo-.... You know what? Nevermind."
    linda_young "Let’s push these losers BACK!"

    # > TAINTED LOVERS (GITAROO MAN OST)
    computer "COMMENCE BATTLE SIMULATION"

    call scene25.camera_redteam
    kohei "This is Ace unit Phoenix, Auxiliary, jam communications. Let’s hit em hard and fast."
    jojo "Carbunkle here, Copy copy."

    call scene25.camera_blueteam
    princess "Diabolos here... Shiva, your boyfriend is coming in hot."
    linda_young "A mistake on his part. Ace unit Shiva here, let’s get in formation!"

    call scene25.camera_redteam
    jojo "JAMMING COMMUNICATIONS!"
    ### page 48 ###
    kohei "Thanks Carbunkle. Alexander, how are we on defense?"
    bart "Support Unit Alexander here: Don’t worry about that, it’s a full offensive push, Ultima Cannon is 70%%. All you’ve got to do is push the lane. I’ll cover you."
    computer "REMOTE SHIELDS ACTIVATED"

    call scene25.camera_blueteam
    huxtable "Support unit Garuda here: the enemy team is pushing lane... maybe we should get into defensive positions..."
    linda_young "You guys know me. I never back down from a fight."
    princess "And I enable her so it’s no use looking at me like that - LET’S GOOO~!"
    computer "REMOTE SHIELDS ACTIVATED"
    princess "How about a nice buff from my personal stash. 35%% should help you fend off yo manz."
    computer "NANO BOTS ACTIVATED, 35%% ATTACK BUFF INSTALLED."
    linda_young "Oh, thank you! Time to CHARGE!"

    call scene25.camera_redteam
    bart "Looks like their ace is meeting us on the battlefield-"
    kohei "With the auxiliary not far behind, what are they thinking."
    ### page 49 ###
    jojo "Guys... I can’t move. I’ve been jammed. Nothing is working."
    bart "They’re debuffing our auxiliary, Ace, you’re gonna have to fight two at one time, and I’m picking up nano tech on their ace, 35%% attack buff."
    kohei "Oh they’re gonna need more than 35%%. Support, help out Aux- The Phoenix is going in."
    return

define redteam_color = '#ff8888'
# define redteam_bg = '#ff4444'
define redteam_bg = '#ffffff'
define blueteam_color = '#8888ff'
# define blueteam_bg = '#4444ff'
define blueteam_bg = '#ffffff'
label scene25.camera_redteam:
    show bg at fx.ease_xpos(1, 0.45, 0.55):
        linear 1.0 matrixcolor TintMatrix(redteam_bg)
    show jojo at fx.ease_xoffset(1, -1200, 0)
    show bart at fx.ease_xoffset(1, -1200, 0)
    show kohei at fx.ease_xoffset(1, -1200, 0)
    show princess at fx.ease_xoffset(1, 0, 1200)
    show huxtable at fx.ease_xoffset(1, 0, 1200)
    show linda at fx.ease_xoffset(1, 0, 1200)
    return

label scene25.camera_blueteam:
    show bg at fx.ease_xpos(1, 0.55, 0.45):
        linear 1.0 matrixcolor TintMatrix(blueteam_bg)
    show jojo at fx.ease_xoffset(1, 0, -1200)
    show bart at fx.ease_xoffset(1, 0, -1200)
    show kohei at fx.ease_xoffset(1, 0, -1200)
    show princess at fx.ease_xoffset(1, 1200, 0)
    show huxtable at fx.ease_xoffset(1, 1200, 0)
    show linda at fx.ease_xoffset(1, 1200, 0)
    return