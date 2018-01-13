label splashscreen:
    play music "splash.wav"
    scene splash0 with fade
    $ renpy.pause(2.0, hard=True)
    scene splash1 with fade
    $ renpy.pause(2.0, hard=True)
init:
    image splash0  = "STMIK.png"
    image splash1 = "splash1.jpg"