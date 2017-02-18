# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image tanya = AttributeImage([
        Attribute("base", "base", "Tanya_base.png", default=True),
        Attribute("emotion", "normal", "eyebrow1.png"),
        Attribute("emotion", "normal", "eye1.png"),
        Attribute("emotion", "normal", "mouth1.png"),
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

    show tanya fire -glasses

    "And this is fire-time."

    show tanya night

    "Good night."
