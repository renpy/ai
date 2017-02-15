# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image tanya = AttributeImage([
        Attribute("base", "base", "Tanya_base.png"),
        Attribute("emotion", "normal", "eyebrow1.png"),
        Attribute("emotion", "normal", "eye1.png"),
        Attribute("emotion", "normal", "mouth1.png"),
        Attribute("glasses", "glasses", "megane.png"),
        Attribute("time", "eve", "overlay_eve.png"),
        Attribute("time", "night", "overlay_night.png"),
        Attribute("time", "fire", "overlay_fire.png"),
        Attribute("time", "day", "overlay_day.png"),
    ],
    image_format="tanya/{image}"
    )



define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tanya base normal glasses eve

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
