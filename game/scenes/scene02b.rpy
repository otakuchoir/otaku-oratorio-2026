label scene02b:
    window hide
    window auto
    show bg scene02 26 with Dissolve(2.0)
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