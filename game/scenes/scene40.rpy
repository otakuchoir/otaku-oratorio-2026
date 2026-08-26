
label scene40:
    scene bg space battlefield
    "PLACEHOLDER IRL: the final battle. we're IRLing the whole scene except for the ending manga panels, right?"

    window hide
    window auto
    # > Usagi, Takeshi and Sanders rush away back to Linda, Kelisha
    # > and Elizabeth. Kagu floats near the Ultima Cannon and then
    # > a huge explosion.
    show bg scene40 explosion 1 at screen_size
    with Dissolve(0.5)
    pause 1.0
    show bg scene40 explosion 2 at screen_size
    with Dissolve(1.0)
    pause 1.0
    show bg scene40 explosion 3 at screen_size
    with Dissolve(1.0)
    pause 1.0
    show bg scene40 explosion 4 at screen_size
    with Dissolve(1.0)
    pause 1.0
    show bg black
    with Dissolve(4.0)

    # > When the picture comes back into view it is
    # > the adult planet destoryer, absorbing the last bits of the
    # > explosion. And staring... Then:
    show bg scene40 judgement 1:
        xsize 1440
        fit "contain"
    with fade
    show bg scene40 judgement 2
    with Dissolve(1.0)
    show bg scene40 judgement 3
    with Dissolve(1.0)
    destroyer "BEAR WITNESS NOW, FOR I AM THE MESSENGER OF THE HEAVENS, THE BEGINNING AND THE END, THE FIRST AND THE LAST. I AM THE GREAT RESETTER; SABIK." with vpunch
    usagi postgrad shock "Oh no... Kagu has fully evolved."
    window hide
    window auto
    show bg scene40 judgement 4
    with Dissolve(1.0)
    destroyer "... YOUR ENTIRE HUMAN RACE... OWES GREAT THANKS TO THE ONE YOU CALL USAGI KITADANI, FOR SHE HAS SHOWN US THE HUMAN POWER OF LOVE AND COMPASSION." with vpunch
    destroyer "THEREFORE, I -WILL- GIVE YOUR SOCIETY A SECOND CHANCE. PRAY THAT WE NEVER MEET AGAIN." with vpunch
    # > In an instant, Sabik is encased in a crystal and disappears
    # > in a flash.
    window hide
    window auto
    pause 0.7
    show bg scene40 judgement 5 with Dissolve(0.3)
    show bg scene40 judgement 6 with Dissolve(0.3)
    show bg scene40 judgement 7 with Dissolve(0.3)
    show bg scene40 judgement 8 with Dissolve(0.5)
    show bg scene40 judgement 9 with Dissolve(3.0)
    pause 1.0
    return