label scene02b:
    show bg scene02 5 with dissolve
    kitadani "LET’S GO! CROWN BLASTER!"
    pause 0
    with vpunch

    # > THE MONSTER DOES NOT FLINCH.
    show bg scene02 1 with dissolve
    monster "Your precious Earth is mine to devour!"

    show bg scene02 5 with dissolve
    kitadani "DAMN!"
    computer "Ultima Cannon ready to dispense justice. Survival rate… 1%%."
    # > KITADANI GLANCES AT THE FAMILY PHOTO ON HIS DASHBOARD
    ### page 3 ###
    kitadani "This is the only way. Justice requires swift action. Citizens of Earth: Lend me your strength! For every human, on this beautiful Earth!"
    show bg scene02 1 with dissolve
    monster "WHAT!?"
    # > Monster reels back to charge it’s atomic breath
    # actually I'm gonna skip this direction because it looks too much like the monster is firing, not the ultima cannon
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
    stop music fadeout 3
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