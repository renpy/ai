# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image tanya = AttributeImage([
        Attribute("base", "base", "Tanya_base.png", default=True),

        Attribute("emotion", "normal", "eyebrow1.png"),
        Attribute("emotion", "happy", "eyebrow1.png"),
        Attribute("emotion", "huh", "eyebrow2.png"),
        Attribute("emotion", "worry", "eyebrow2.png"),

        Attribute("emotion", "normal", "eye1.png", pos=(100, 0)),
        Attribute("emotion", "happy", "eye1.png"),
        Attribute("emotion", "huh", "eye3.png"),
        Attribute("emotion", "worry", "eye1.png"),

        Attribute("emotion", "normal", "mouth1.png"),
        Attribute("emotion", "happy", "mouth2.png"),
        Attribute("emotion", "huh", "mouth3.png"),
        Attribute("emotion", "worry", "mouth1.png"),

        Attribute("glasses", "glasses", "megane.png"),

        Attribute("time", "eve", "overlay_eve.png", default=True),
        Attribute("time", "night", "overlay_night.png"),
        Attribute("time", "fire", "overlay_fire.png"),
        Attribute("time", "day", "overlay_day.png"),
    ],
    image_format="tanya/{image}"
    )


label main_menu:
    return


label start:

    show tanya normal glasses

    "This is the normal mood."

    show tanya happy fire -glasses

    "And this is fire-time."

    show tanya night

    "Good night."
