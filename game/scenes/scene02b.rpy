label scene02b:
    show bg scene02 08 with dissolve
    show bg scene02 09 with dissolve
    kitadani "LET’S GO! CROWN BLASTER!"

    # > THE MONSTER DOES NOT FLINCH.
    show bg scene02 10 with dissolve
    with vpunch
    pause 1.5
    show bg scene02 11 with dissolve
    pause 1.5
    show bg scene02 12 with dissolve
    monster "Your precious Earth is mine to devour!"

    window hide
    window auto
    show bg scene02 13 with dissolve
    pause 1.0
    show bg scene02 14 with dissolve
    pause 2.0
    show bg scene02 15 with dissolve
    kitadani "DAMN!"

    window hide
    window auto
    show bg scene02 16 with dissolve
    pause 2.0
    show bg scene02 17 with dissolve
    computer "Ultima Cannon ready to dispense justice. Survival rate… 1%%."

    window hide
    window auto
    show bg scene02 18 with dissolve
    pause 1.5
    show bg scene02 19 with dissolve
    pause 2.0
    show bg scene02 20 with dissolve
    # > KITADANI GLANCES AT THE FAMILY PHOTO ON HIS DASHBOARD
    ### page 3 ###
    kitadani "This is the only way. Justice requires swift action. Citizens of Earth: Lend me your strength! For every human, on this beautiful Earth!"
    show bg scene02 21 with dissolve
    monster "WHAT!?"
    # > Monster reels back to charge it’s atomic breath
    # actually I'm gonna skip this direction because it looks too much like the monster is firing, not the ultima cannon
    show bg scene02 22 with dissolve
    kitadani "Ultima Cannon: {b}FIRE!{/b}"
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