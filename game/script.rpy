# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tanya", image="tanya")

attributeimage tanya:

    image_format "tanya/{image}"

    attribute base "Tanya_base.png":
        default True

    group emotion:
        attribute normal "eyebrow1.png"
        attribute happy "eyebrow1.png"
        attribute huh "eyebrow2.png"
        attribute worry "eyebrow2.png"

    group emotion:
        attribute normal "eye1.png"
        attribute happy "eye1.png"
        attribute huh "eye3.png"
        attribute worry "eye1.png"

    group emotion:
        attribute normal "mouth1.png"
        attribute happy "mouth2.png"
        attribute huh "mouth3.png"
        attribute worry "mouth1.png"


    if glasses:
        "megane.png"

    group time:

        attribute eve "overlay_eve.png":
            default True

        attribute night "overlay_night.png"
        attribute fire "overlay_fire.png"
        attribute day "overlay_day.png"


#
# image tanya = AttributeImage([
#         Attribute("base", "base", "Tanya_base.png", default=True),
#
#         Attribute("emotion", "normal", "eyebrow1.png"),
#         Attribute("emotion", "happy", "eyebrow1.png"),
#         Attribute("emotion", "huh", "eyebrow2.png"),
#         Attribute("emotion", "worry", "eyebrow2.png"),
#
#         Attribute("emotion", "normal", "eye1.png"),
#         Attribute("emotion", "happy", "eye1.png"),
#         Attribute("emotion", "huh", "eye3.png"),
#         Attribute("emotion", "worry", "eye1.png"),
#
#         Attribute("emotion", "normal", "mouth1.png"),
#         Attribute("emotion", "happy", "mouth2.png"),
#         Attribute("emotion", "huh", "mouth3.png"),
#         Attribute("emotion", "worry", "mouth1.png"),
#
#         ConditionGroup([
#             Condition("glasses", "megane.png"),
#             ]),
#
#         Attribute("time", "eve", "overlay_eve.png", default=True),
#         Attribute("time", "night", "overlay_night.png"),
#         Attribute("time", "fire", "overlay_fire.png"),
#         Attribute("time", "day", "overlay_day.png"),
#     ],
#     image_format="tanya/{image}",
#     at=right,
#     )


image side tanya = AttributeImage([
        Attribute("base", "base", "Tanya_base.png", default=True),

        Attribute("emotion", "normal", "eyebrow1.png"),
        Attribute("emotion", "happy", "eyebrow1.png"),
        Attribute("emotion", "huh", "eyebrow2.png"),
        Attribute("emotion", "worry", "eyebrow2.png"),

        Attribute("emotion", "normal", "eye1.png"),
        Attribute("emotion", "happy", "eye1.png"),
        Attribute("emotion", "huh", "eye3.png"),
        Attribute("emotion", "worry", "eye1.png"),

        Attribute("emotion", "normal", "mouth1.png"),
        Attribute("emotion", "happy", "mouth2.png"),
        Attribute("emotion", "huh", "mouth3.png"),
        Attribute("emotion", "worry", "mouth1.png"),

        Condition("glasses", "megane.png"),

        Attribute("time", "eve", "overlay_eve.png", default=True),
        Attribute("time", "night", "overlay_night.png"),
        Attribute("time", "fire", "overlay_fire.png"),
        Attribute("time", "day", "overlay_day.png"),
    ],
    image_format="tanya/{image}",
    at=Transform(zoom=0.5, xalign=0.0, yalign=1.0),
    )

label main_menu:
    return


default glasses = True

label start:

    menu:
        "Glasses.":
            $ glasses = True
        "No glasses.":
            $ glasses = False


    show tanya normal

    pause

    show tanya

    t "This is the normal mood."

    show tanya happy fire
    with dissolve

    t "And this is fire-time."

    show tanya night

    t "Good night."
