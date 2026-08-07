
label scene02:
    scene bg jersey city cityscape
    "PLACEHOLDER manga panels: postcard memories (temporary background)"
    # > 2        EXT. CITY MONSTER ATTACK                                                  2
    # > A RUBBER-SUITED GODZILLA-STYLE PLANET DESTROYER STOMPS
    # > THROUGH MODEL CITY, BURNING BUILDINGS WITH ATOMIC BREATH
    # > A HERO DRESSED IN RED RUNS IN, DRAMATICALLY SKIDDING ON TO
    # > THE SCENE AS THEIR SCARF BLOWS IN THE WIND DRAMATICALLY.
    announcer "Oh no! The monster is destroying the city! Can anybody stop this?"
    kitadani "Fear not, announcer! Courageous Kaito! Reporting for Duty!"
    announcer "When chaos calls, the Crown answers swiftly with its bravest warrior: Sea Jetter Kai!"
    kitadani "LET’S GO! CROWN BLASTER!"
    pause 0
    with vpunch
    # > 
    # >          SONG: Fumetsu no Hero    # > 
    "PLACEHOLDER Song: Fumetsu no Hero"
    # > THE MONSTER DOES NOT FLINCH.
    monster "Your precious Earth is mine to devour!"
    # > MONSTER EATS MINIATURE BUILDING COOKIE MONSTER STYLE
    show bg jersey city cityscape as eat1:
        xpos 450
        ypos 100
        crop (0, 100, 150, 200)
    with hpunch
    show bg jersey city cityscape as eat2:
        xpos 450
        ypos 300
        crop (0, 300, 150, 200)
    with vpunch
    show bg jersey city cityscape as eat3:
        xpos 450
        ypos 500
        crop (0, 400, 150, 150)
    with hpunch
    kitadani "DAMN!"
    computer "Ultima Cannon ready to dispense justice. Survival rate… 1%%."
    # > KITADANI GLANCES AT THE FAMILY PHOTO ON HIS DASHBOARD
    ### page 3 ###
    kitadani "This is the only way. Justice requires swift action. Citizens of Earth: Lend me your strength! For every human, on this beautiful Earth!"
    monster "WHAT!?"
    # > Monster reels back to charge it’s atomic breath
    kitadani "Ultima Cannon: fire!"
    show bg white as boom:
        alpha 0
        linear 1.5 alpha 1
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    scene bg black
    with dissolve
    announcer "Kono bangumi wa, goran no suponsaa no teikyou de okurishimasu."
    # > PROJECTOR: “THIS CROWN NETWORK MEMORIAL SEGMENT WAS BROUGHT
    # > TO YOU BY THE FOLLOWING SPONSORS:”
    # > PROJECTOR:; IN MEMORY OF KOHEI KITADANI

    show text "{color=#fff}{size=80}THIS CROWN NETWORK\nMEMORIAL SEGMENT\nWAS BROUGHT TO YOU BY\nTHE FOLLOWING SPONSORS:{/size}{/color}" at truecenter with dissolve
    pause
    hide text with dissolve
    show text "{color=#fff}{size=160}IN MEMORY OF\nKOHEI KITADANI{/size}{/color}" at truecenter with dissolve
    pause
    hide text with dissolve
    return